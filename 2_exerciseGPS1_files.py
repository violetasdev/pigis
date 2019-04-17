#################################
# Python in GIS  - Exercise 2b #
# Date: 17/04/2019             #
################################

import os,sys

#Place the gpx file you have downloaded from www.gpsies.com in a convenient folder, e.g. …/pythonGIS/data
#Write a function, using the os library, to check for the existence of the file

def existFile(routeFile):
    #If the file exists, the function should open it (simply with open) and return the contents
    if os.path.exists(routeFile) == True:
        content=open(routeFile,"r")
        print(content.read())
    #If it does not exist, the function should return None
    else:
        print('There is no file: None')


gpspath='C:\\Users\\Violet\\Documents\\Master\\Europa\\Clases Alemania\\Python in GIS\\code\\pigis\\data\\Witten82.gpx'
gpspath_fixed=(os.path.join('C:\\','Users','Violet','Documents','Master','Europa','Clases Alemania','Python in GIS','code','pigis','data','Witten82.gpx'))

existFile(gpspath)
existFile(gpspath_fixed)
existFile('sdfsdf')
#In the main part of the script, call the function and print the contents of the file
#Run the script in QGIS

#Test it with both a correct and incorrect path
