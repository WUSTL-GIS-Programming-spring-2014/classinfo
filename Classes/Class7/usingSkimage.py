import arcpy
import skimage.filter

# Using a subset to avoid memory problems. This is better in 64-bit.
test = arcpy.Clip_management("027-044_rgb.tif","749250 1127500 750250 1128000", "test") 

# Convert our raster image to a numpy array.
nimg = arcpy.RasterToNumPyArray("test")

# Break out each band of the image for edge detection.
rband = nimg[0]
gband = nimg[1]
bband = nimg[2]

#Detect edges with the Sobel filter.
redge = skimage.filter.sobel(rband)
gedge = skimage.filter.sobel(gband)
bedge = skimage.filter.sobel(bband)

#Composite results and make raster.
edges = redge + gedge + bedge
eimg = arcpy.NumPyArrayToRaster(edges,arcpy.Point(749250,1127500), 0.5, 0.5)
eimg.save(u'sobeledges')

#Detect edges with the Canny filter.
rcanny = skimage.filter.canny(rband)
gcanny = skimage.filter.canny(gband)
bcanny = skimage.filter.canny(bband)

#Composite results and make raster.
cannyedges = rcanny.astype(int) + gcanny.astype(int) + bcanny.astype(int)
cimg =  arcpy.NumPyArrayToRaster(cannyedges,arcpy.Point(749250,1127500), 0.5, 0.5)
cimg.save(u'cannyedges')
