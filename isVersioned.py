import arcpy
from arcpy import env
schemas=["ASSETMAN","CARTO","ENV"]
            
for x in schemas:
    env.workspace= r'Database Connections' + x
    fcList=arcpy.ListFeatureClasses()
    for fc in fcList:
        try:
            datasetVersioned = arcpy.Describe(fc).isVersioned
            if str(datasetVersioned) == "False":
                print str(datasetVersioned) + " " + fc + "-------> " + x
        except IOError:
            print "IOError Found" + fc
            continue
    ftList=arcpy.ListTables()
    for ft in ftList:
        try:
            datasetVersioned = arcpy.Describe(ft).isVersioned
            if str(datasetVersioned) == "False":
                print str(datasetVersioned) + " " + ft + "-------> " + x
        except IOError:
            print "IOError Found" + ft
            continue
    fdList=arcpy.ListDatasets()
    for fd in fdList:
        try:
            datasetVersioned = arcpy.Describe(fd).isVersioned
            if str(datasetVersioned) == "False":
                print str(datasetVersioned) + " " + fd + "-------> " + x
        except IOError:
            print "IOError Found" + fd
            continue

env.workspace="Database Connections"
fcList=arcpy.ListFeatureClasses()
for fc in fcList:
    try:
        datasetVersioned = arcpy.Describe(fc).isVersioned
        if str(datasetVersioned) == "False":
            print str(datasetVersioned) + " " + fc
    except IOError:
        print "IOError Found" + fc
        continue
   
ftList=arcpy.ListTables()
for ft in ftList:
    try:
        datasetVersioned = arcpy.Describe(ft).isVersioned
        if str(datasetVersioned) == "False":
            print str(datasetVersioned) + " " + ft
    except IOError:
        print "IOError Found" + ft
        continue
 
fdList=arcpy.ListDatasets()
for fd in fdList:
    try:
        datasetVersioned = arcpy.Describe(fd).isVersioned
        if str(datasetVersioned) == "False":
            print str(datasetVersioned) + " " + fd 
    except IOError:
        print "IOError Found" + fd
        continue
  

    
