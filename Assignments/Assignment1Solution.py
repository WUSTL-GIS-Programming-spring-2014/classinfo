# Your name here
# Assignment 1: Batch Geoprocessing

import arcpy

def main(shapefiles,prefix):
    """Buffer a list of input shapefiles, prefixing the new files."""
    # Assume all shapefiles are in workspace and output to workspace.
    # Loop through list parameter shapefiles.
    for shapefile in shapefiles:
        # Create output filename for each input shapefile.
        output = prefix + shapefile
        #Run Buffer than loop to next shapefile. Distance is hardcoded.
        arcpy.Buffer_analysis (shapefile, output, u'500 Feet')

if __name__ == '__main__':
    # Add workspace here along with other arguments.
    arcpy.env.workspace = u'C:\\arcgis'
    # This is a list of two shapefiles, corresponding to u'C:\\arcgis\\Schools.shp' and u'C:\\arcgis\\Daycares.shp'
    s = [u'Schools.shp', u'Daycares.shp']
    # This is the prefix that will be prepended onto each filename to give an output file name.
    prefix = u'Buffered_500Feet_'
    # Call main() when script is run instead of imported.
    main(s, prefix)
