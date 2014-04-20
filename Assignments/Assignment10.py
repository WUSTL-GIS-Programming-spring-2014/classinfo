# (Place your name here in a comment)
# Assignment 10: NDVI with rasterio
# Note: NDVI = (IR - R)/(IR + R)
# Use the same data as Assignmetn 5 at https://www.dropbox.com/s/lo91vpjlh7c0a5i/Assignment5.gdb.zip
# You can convert to whatever image format you would like, or I will provide a sample tif on Monday.
import os
import rasterio

def main(imagepath,outputpath):
    """Calculate NDVI using rasterio."""
    #Using rasterio.drivers(), read in the infrared and red band from the image
    #Make sure to use float

    #Calculate the output raster using numpy as in this example: https://github.com/mapbox/rasterio/blob/master/examples/total.py
    #Though do not use the += and /= shorthand
    
    #Write the new image back out in the format of your choice
    return output #Make sure this is a string representing the path to the NDVI image
    

# Call your main function when program is executed.
# This allows import without executing the main function
if __name__ == '__main__':
    os.chmod(<root directory>)
    imagepath = u'path to image'
    print main(imagepath,outputpath)
