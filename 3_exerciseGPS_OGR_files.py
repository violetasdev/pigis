#################################
# Python in GIS  - Exercise 3  #
# Date: 18/04/2019             #
################################

#Convert the GPS track you have to a shapefile using OGR in Python (in QGIS).
#Hint: Do not only rely on the messages Python gives, also check the output files

import ogr,os


# reading a shapefile
gps_source=None
in_dir = os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data')
in_path = os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data','Witten82.gpx')

# get the correct driver
in_driver = ogr.GetDriverByName('GPX')
gps_source = in_driver.Open(in_path, 0)

# write the data to a shp
out_file = os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data','Witten82.shp')
out_driver = ogr.GetDriverByName('ESRI Shapefile')
out_ds  = out_driver.CopyDataSource(gps_source,out_file)

del out_ds

out_shapes=[]
count=0
for file in os.listdir(in_dir):
    if file.endswith('.shp'):
        out_shapes.append(os.path.join(in_dir, file))
        count=++count


print('Total Shapesfiles generated: %s' % len(out_shapes))
print()

#If you still have time: Write a script to find the field names and the nr of attributes of your new shapefile

def returnShpCount(shapePath):
    driver = ogr.GetDriverByName('ESRI Shapefile')
    data_source = driver.Open(shapePath, 0)
    # Check to see if shapefile is found.
    if data_source is None:
        print('Could not open %s' % (shapePath))
    else:
        print('Opened %s' % (shapePath ))
        # get the Layer class object
        layer = data_source.GetLayer(0)
        # get info about the attributes (fields)
        attributes = layer.GetLayerDefn()

        for i in range(attributes.GetFieldCount()):
            print(attributes.GetFieldDefn(i).GetName(),end="\t")


        print("\n\nNumber of attributes in %s: %d" % (os.path.basename(shapePath),attributes.GetFieldCount()))

for shapes in out_shapes:
    returnShpCount(shapes)
    print()
