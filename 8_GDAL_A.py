#Using GDAl to open and process the DEM for our GPX track
#Load the GPS shapefile with added time_str field and removed empty fields


#libraries
import gdal, osr, os

#directories
data_dir=(os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS'))
#Load the elevation raster
#path to raster
in_path=os.path.join(data_dir,'GermanyDGM1','dgm1_5meter.img')
#open raster
raster_data_source=gdal.Open(in_path)
print(raster_data_source)

#Check the spatial reference system of both datasets (you will see that they are different)
#get georeference info raster
rast_spatial_ref=raster_data_source.GetProjection()
print('raster spatial ref is:',rast_spatial_ref)
print('type rast_spatial_ref:',type(rast_spatial_ref))

sr_raster=osr.SpatialReference(rast_spatial_ref)
print('raster spatial ref is',sr_raster)
print(sr_raster.GetAttrValue('PROJECTION'))

#get georeference info gpx track

#Project the GPS track to the same projection as the raster
