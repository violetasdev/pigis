#Using GDAl to open and process the DEM for our GPX track
#Load the GPS shapefile with added time_str field and removed empty fields


#libraries
import gdal, osr, os,ogr

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
driver = ogr.GetDriverByName('ESRI Shapefile')
shape_file = os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data','clean_layer.shp')
dataset = driver.Open(shape_file)

in_layer=dataset.GetLayer()
shape_spatial_ref=in_layer.GetSpatialRef()

print('shape spatial ref is:',shape_spatial_ref)
print('type shape_spatial_ref:',type(shape_spatial_ref))

#Project the GPS track to the same projection as the raster
coordTrans=osr.CoordinateTransformation(shape_spatial_ref,sr_raster)
outputLayer=os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data','reprojected_clean_layer.shp')

##outputLayer
if os.path.exists(outputLayer):
    driver.DeleteDataSource(outputLayer)
outDataSet = driver.CreateDataSource(outputLayer)
outLayer = outDataSet.CreateLayer("projectedTrack", geom_type=ogr.wkbPoint)
out_defn=outLayer.GetLayerDefn()

out_feat=ogr.Feature(out_defn)
##Assign the transformed geometry to the feature
inLayerDefn = in_layer.GetLayerDefn()
for i in range(0, inLayerDefn.GetFieldCount()):
    fieldDefn = inLayerDefn.GetFieldDefn(i)
    outLayer.CreateField(fieldDefn)

# get the output layer's feature definition
out_defn = outLayer.GetLayerDefn()

# loop through the input features
inFeature = in_layer.GetNextFeature()
while inFeature:
    # get the input geometry
    geom = inFeature.GetGeometryRef()
    # reproject the geometry
    geom.Transform(coordTrans)
    # create a new feature
    outFeature = ogr.Feature(out_defn)
    # set the geometry and attribute
    outFeature.SetGeometry(geom)
    for i in range(0, out_defn.GetFieldCount()):
        outFeature.SetField(out_def.GetFieldDefn(i).GetNameRef(), inFeature.GetField(i))
    # add the feature to the shapefile
    outLayer.CreateFeature(outFeature)
    # dereference the features and get the next input feature
    outFeature = None
    inFeature = inLayer.GetNextFeature()
