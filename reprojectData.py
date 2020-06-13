import arcpy
try:
    arcpy.env.workspace = arcpy.GetParameterAsText(0)
    # feature class, who has correct SR
    inputFC = arcpy.GetParameterAsText(1)

    # get spatial reference for the input feature class
    inputDescribe = arcpy.Describe(inputFC)
    inputSR = inputDescribe.SpatialReference
    inputSRName = inputSR.Name

    # create a list of FeatureClasses
    listFC = arcpy.ListFeatureClasses()
except:
    arcpy.AddError("Could not get correct parameters")

for i in listFC:
    fcDescribe = arcpy.Describe(i)
    fcSR = fcDescribe.SpatialReference
    fcSRName = fcSR.Name

    if fcSRName == inputSRName:
        continue
    else:
        # create output feature class path and its name
        outFS = i[:-4] + "_projected.shp"
        arcpy.Project_management(i, outFS, inputSR)
        arcpy.AddMessage("Projected " + str(outFS))
