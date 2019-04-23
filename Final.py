import arcpy
from arcpy import env
env.workspace = "C:\Users\seong\Desktop\Seonghun\GEOG 380\Final Project"

#Creating a new field for "Assault" type of crime
arcpy.Addfield_management("point", "assaults", "TEXT")

#Using Cursor to validate and assign values into the "assault" field
with arcpy.da.UpdateCursor("point", ['Offence Ca', 'assaults']) as cursor:
    #using for loop to loop through the "Offence Ca" to find all the "ASSAULT" and assigning them into new "assault" field.
    for row in cursor:
        if row[0] == "ASSAULT":
            row[1] = "Assault"
            cursor.updateRow(row)
            
#Creating a new field for "Time" of crime
arcpy.Addfield_management("point", "Time", "TEXT")

#Using Cursor to validate and assign values into the "Time" field
with arcpy.da.UpdateCursor("point",['Hour of Da', 'Time']) as cursor:
    #using for loop to loop through the "Hour of Da" to find all the different times the crime occured.
    for t in cursor:
        time = t[0]
        if 5 < time < 12:
            t[1] = "Morning"
        if 11 < time < 18:
           t[1] = "Afternoon"
        if 17 < time < 24:
           t[1] = "Night"
        else:
           t[1] = "Late Night"
        cursor.updateRow(t)

#Creating a new field for "Burg_Theft" type of crime
arcpy.Addfield_management("point", "Burg_Theft", "TEXT")

#Using Cursor to validate and assign values into the "Burg_Theft" field
with arcpy.da.UpdateCursor("point", ['Offence Ca', 'Burg_Theft']) as cursor:
    #using for loop to loop through the "Offence Ca" to find all the burgalary/stolen related crimes and assigning them into the "Burg_Theft" field.
    for row in cursor:
        name = row[0]
        if name in ["BURGLARY", "STOLEN VEHICLE", "STOLEN PROPERTY"]:
            row[1] = "Stolen"
            cursor.updateRow(row)

arcpy.Statistics_analysis("point")....



# Local variables:
detroit = "detroit"
point = "point"
stats = "C:\\Users\\eiarhabi\\Documents\\ArcGIS\\Default.gdb\\detroit_SpatialJoin"

# Process: Spatial Join
arcpy.SpatialJoin_analysis(detroit, point, stats)
