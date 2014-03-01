# (Place your name here in a comment)
# Assignment 5: NDVI
# Note: NDVI = (IR - R)/(IR + R)

import arcpy

def getBands():
    """Returns a tuple of two single band rasters, a red band and an infrared band."""
    #I will supply this function once I have a sample RGBI image from the NAIP
    return (redband,irband)

def mapalgebraNDVI(bands):
    """Given a tuple of two rasters representing a red band and an ir band, calculate NDVI using map algebra."""
    redband,irband = bands
    #Do your NDVI calculation here using only map algebra.
    
    #Assign your result to the variable 'moutput'.
    return moutput

def numpyNDVI(redband,irband):
    """Given a tuple of two rasters representing a red band and an ir band, calculate NDVI using numpy."""
    redband,irband = bands
    #Convert the input bands to numpy arrays.

    #Do your NDVI calculation here using numpy.
    
    #Convert back to a raster.
    #Assign your result to the variable 'noutput'.
    return noutput

def main():
    """Calculate NDVI in two different ways."""
    arcpy.env.workspace = u'Your workspace'
    mNDVI = mapalgebraNDVI(getbands)
    nNDVI = numpyNDVI(numpy)
    #Save mNDVI as u'mNDVI' and nNDVI as u'nNDVI' when you are done


# Call your main function when program is executed.
# This allows import without executing the main function
if __name__ == '__main__':
    main()

