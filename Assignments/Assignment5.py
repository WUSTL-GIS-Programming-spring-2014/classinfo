# (Place your name here in a comment)
# Assignment 5: NDVI
# Note: NDVI = (IR - R)/(IR + R)
# Geodatabase available on Dropbox at https://www.dropbox.com/s/lo91vpjlh7c0a5i/Assignment5.gdb.zip

import arcpy

def getBands():
    """Returns a tuple of two single band rasters, a red band and an infrared band."""
    bands = arcpy.ListRasters()
    try:
        redband = arcpy.Raster(u'faustRed')
    except Exception as e:
        if (u'faustRed' not in bands):
            print '\'faustRed\' not available. Is your workspace set to the geodatabase containing \'faustRed\'?'
        raise e
    try:
        irband = arcpy.Raster(u'faustRed')
    except Exception as e:
        if (u'faustIR' not in bands):
            print '\'faustIR\' not available. Is your workspace set to the geodatabase containing \'faustIR\'?'
        raise e
    return (redband,irband)

def mapalgebraNDVI(bands):
    """Given a tuple of two rasters representing a red band and an ir band, calculate NDVI using map algebra."""
    redband,irband = bands
    #Convert your bands to float using arcpy.sa.Float
    #Do your NDVI calculation here using only map algebra.
    
    #Assign your result to the variable 'moutput'.
    return moutput

def numpyNDVI(redband,irband):
    """Given a tuple of two rasters representing a red band and an ir band, calculate NDVI using numpy."""
    redband,irband = bands
    #Convert the input bands to numpy arrays.
    #Convert your arrays to float using array.astype(float)

    #Do your NDVI calculation here using numpy.
    
    #Convert back to a raster.
    #Remember to assign the correct lower left corner and cell dimensions
    #Assign your result to the variable 'noutput'.
    return noutput

def main():
    """Calculate NDVI in two different ways."""
    arcpy.env.workspace = u'Your workspace' #Set your workspace to the assignment geodatabase on your computer
    mNDVI = mapalgebraNDVI(getbands)
    nNDVI = numpyNDVI(numpy)
    #Save mNDVI as u'mNDVI' and nNDVI as u'nNDVI' when you are done


# Call your main function when program is executed.
# This allows import without executing the main function
if __name__ == '__main__':
    main()

