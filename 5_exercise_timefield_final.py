#################################
# Python in GIS  - Exercise 5  #
# Date: 25/04/2019             #
################################

#1. Manually add the track points from the original gps waypoints (track_points) to QGIS


import os
from qgis.core import *
import qgis.utils

#2. In the script: select active layer and get the QgsVectorLayer() object of the gpx
layer = qgis.utils.iface.activeLayer();
layer.id();
print(layer.featureCount())

dictionary=dict()
features = layer.getFeatures()
for feature in features:
    # retrieve id and attribute values
    #print("Feature ID: %d " % feature.id())
    attributes = feature.attributes()
    # attributes is a list
    for field, attr in zip(layer.fields(), attributes):
        if field.name()=='time':
            dictionary[feature.id()]=attr.toString('hh:mm:ss')
            #print(field.name(), ':', attr.toString('hh:mm:ss'))

#for field in layer.fields():
#    print(field.name(), field.typeName())

for idgpx in dictionary:
    print(idgpx)
    if idgpx==5:break

#3. Load the shapefile
shape_file = os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data','track_points.shp')
layerShp=iface.addVectorLayer(shape_file,"shape:","ogr")

if not layer:
    print("Shapefile track_points could not be loaded!")

for field in layerShp.fields():
    print (field.name(),field.typeName())

#4. Add a field to the shapefile: ‘time_str’ (time as a String)
caps=layerShp.dataProvider().capabilities()

#if caps & QgsVectorDataProvider.AddAttributes:
#    res=layer.dataProvider().addAttributes([QgsField("time_str",QVariant.String)])
layerShp.updateFields()

#5. For each feature in the gpx: Copy to the time from date_time field to a dictionary
# with as the key the id of that feature
# (Remember how to get the time from a datetime object from the basic lib lecture)

#6. Update for all features in the shapefile the new ‘time_str’ attribute
featuresShp = layerShp.getFeatures()
for featureShp in featuresShp:
    # retrieve id and attribute values
    print("Feature ID: %d " % featureShp.id())
    if caps & QgsVectorDataProvider.ChangeAttributeValues:
        attrs={26:dictionary[featureShp.id()]}
        layerShp.dataProvider().changeAttributeValues({featureShp.id():attrs})
        #if featureShp.id()==5:break
