# (Place your name here in a comment)
# Assignment 4: Using Cursors


# Use the filegeodatabase at https://www.dropbox.com/s/lcjodja7ix8oruh/Assignment4.gdb.zip
#You should only need arcpy for this assignment
import arcpy

def idToSchool(i):
    """When provided a valid district id from '088' to '119', returns the name of the school district"""
    district = [u'HAZELWOOD', u'FERGUSON-FLORISSANT', u'PATTONVILLE', u'ROCKWOOD', u'KIRKWOOD', u'LINDBERGH', u'MEHLVILLE', u'PARKWAY', u'', u'', u'AFFTON', u'BAYLESS', u'', u'BRENTWOOD', u'CLAYTON', u'HANCOCK PLACE', u'JENNINGS', u'', u'LADUE', u'MAPLEWOOD-RICHMOND HEIGHTS', u'', u'NORMANDY', u'RITENOUR', u'RIVERVIEW GARDENS', u'UNIVERSITY CITY', u'VALLEY PARK', u'WEBSTER GROVES', u'', u'', u'', u'', u'SPECIAL SCHOOL DISTRICT']
    s = dict(zip([str(x).zfill(3) for x in range(88,120)], district))
    try:
        return s[str(i).zfill(3)]
    except KeyError:
        return u''

    

# Place your code in a main() function.
# Comment in complete sentences.  Use two spaces between sentences.
def main():
    """Create a new PublicSchools feature class for St Louis County based on latest DESE information, schoolPublicDESE."""
    # Do NOT modify the DESE feature class.
    
    # Create the empty feature class PublicSchools, templated on schoolPublic with a District field added
    d = arcpy.Describe(u'schoolPublicDESE')
    arcpy.CreateFeatureclass_management(arcpy.env.workspace, u'PublicSchools',"POINT", u'schoolPublicDESE',"SAME_AS_TEMPLATE", "SAME_AS_TEMPLATE",d.spatialReference)
    arcpy.AddField_management("PublicSchools","District","TEXT")
    
    # Create an insert cursor for the new empty feature class with an appropriate field list
    insertSchool = arcpy.da.InsertCursor("PublicSchools,<Field List>)

    # Create a search cursor to loop through all the St Louis County (ID 096) schools and insert them
    # into PublicSchools with the appropriate school district in title case in the District field
    # Hint: The county ID is the first three characters of CtyDist. The district ID is the last three charactrers

    # Make sure to appropriately clean up both the searchCursor and the insertCursor, even if there is an error!

# Call your main function when program is executed.
# This allows import without executing the main function
if __name__ == '__main__':
    # Set an appropriate path for your workspace
    arcpy.env.workspace = u'C:\\arcgis\\Assignment4.gdb'
    main()
