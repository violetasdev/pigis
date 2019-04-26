#################################
# Python in GIS  - Exercise 5  #
# Date: 25/04/2019             #
################################

#1. Manually add the track points from the original gps waypoints (track_points) to QGIS


import os
from qgis.core import *
import qgis.utils

#2. In the script: select active layer and get the QgsVectorLayer() object of the gpx
layer= iface.activeLayer()
print (layer)

#3. Load the shapefile
shape_file = os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data','track_points.shp')
layer=iface.addVectorLayer(shape_file,"shape:","ogr")
if not layer:
    print("Shapefile track_points could not be loaded!")

for field in layer.fields():
    print (field.name(),field.typeName())

#4. Add a field to the shapefile: ‘time_str’ (time as a String)
caps=layer.dataProvider().capabilities()

if caps & QgsVectorDataProvider.AddAttributes:
#    res=layer.dataProvider().addAttributes([QgsField("time_str",QVariant.String)])

layer.updateFields()

#5. For each feature in the gpx: Copy to the time from date_time field to a dictionary
# with as the key the id of that feature
# (Remember how to get the time from a datetime object from the basic lib lecture)
gpx_source=None
gpx_path = os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data','Witten82.gpx')
in_driver = ogr.GetDriverByName('GPX')
gpx_source = in_driver.Open(gpx_path, 0)
print(gpx_source)

# Check to see if file is find
if gpx_source is None:
    print('Could not open %s' % (gpx_path))
else:
    print('Opened %s' % (gpx_path))
    layergpx = gpx_source.GetLayer(0)
    featureCount = layergpx.GetFeatureCount()
    print("Number of features in %s: %d" % \(os.path.basename(gpx_path),featureCount))


#6. Update for all features in the shapefile the new ‘time_str’ attribute


















#################################
# Python in GIS  - Exercise 5  #
# Date: 25/04/2019             #
################################

#1. Manually add the track points from the original gps waypoints (track_points) to QGIS


import os
from qgis.core import *
import qgis.utils

#2. In the script: select active layer and get the QgsVectorLayer() object of the gpx
layer= iface.activeLayer()
print (layer)

#3. Load the shapefile
shape_file = os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data','track_points.shp')
layer=iface.addVectorLayer(shape_file,"shape:","ogr")
if not layer:
    print("Shapefile track_points could not be loaded!")

for field in layer.fields():
    print (field.name(),field.typeName())

#4. Add a field to the shapefile: ‘time_str’ (time as a String)
caps=layer.dataProvider().capabilities()

#if caps & QgsVectorDataProvider.AddAttributes:
#    res=layer.dataProvider().addAttributes([QgsField("time_str",QVariant.String)])

layer.updateFields()

#5. For each feature in the gpx: Copy to the time from date_time field to a dictionary
# with as the key the id of that feature
# (Remember how to get the time from a datetime object from the basic lib lecture)
gpx_source=None
gpx_path = os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data','Witten82.gpx')
in_driver = ogr.GetDriverByName('GPX')
gpx_source = in_driver.Open(gpx_path, 0)
print(gpx_source)

# Check to see if file is find
if gpx_source is None:
    print('Could not open %s' % (gpx_path))
else:
    print('Opened %s' % (gpx_path))
    layergpx = gpx_source.GetLayer(0)

    print(layergpx)

    featureCount = layergpx.GetFeatureCount()
    print("Number of features in %s: %d" % (os.path.basename(gpx_path),featureCount))


#6. Update for all features in the shapefile the new ‘time_str’ attribute
