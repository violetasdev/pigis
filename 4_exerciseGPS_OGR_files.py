
import os,sys,ogr

gpspath='C:\\Users\\Violet\\Documents\\Master\\Europa\\Clases Alemania\\Python in GIS\\code\\pigis\\data\\Witten82.gpx'
data_dir=(os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data'))
gps_datasource=None

driver=ogr.GetDriverByName('GPX')

#GPSTrackMaker GPX
gps_datasource=driver.Open(gpspath,0)

if gps_datasource is None:
    print('Could not open %s' % (in_path))
else:
    print('File is open')

print('Opened %s' % (in_path))
# get the Layer class object
layer = data_source.GetLayer(0)
# get reference system info
spatial_ref = layer.GetSpatialRef()
print(spatial_ref)





# Create the output file
out_fn = os.path.join(data_dir, 'trackGPS.shp')
# Delete if output file already exists
# We can use the same driver
if os.path.exists(out_fn):
    print('exists, deleting')
    driver.DeleteDataSource(out_fn)
out_ds = driver.CreateDataSource(out_fn)
if out_ds is None:
    print('Could not open %s' % (out_fn))

# Create the shapefile layer.
out_lyr = out_ds.CreateLayer('trackPoint',in_lyr.GetSpatialRef(),ogr.wkbPoint)

out_lyr.CreateFields(in_lyr.schema)
out_defn = out_lyr.GetLayerDefn()
out_feat = ogr.Feature(out_defn)




import ogr
import os

# reading a shapefile
in_path = os.path.join(os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data','Witten82.gpx')

# get the correct driver
in_driver = ogr.GetDriverByName('GPX')
places_source = in_driver.Open(in_path, 0)

print(places_source)

# write the data to a shapefile
out_file = os.path.join(os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data','Witten82.shp')
out_driver = ogr.GetDriverByName('ESRI Shapefile')
out_ds  = out_driver.CopyDataSource(places_source,out_file)
del out_ds
