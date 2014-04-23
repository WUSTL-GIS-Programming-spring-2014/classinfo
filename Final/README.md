# Exam concept
The concept of this exam is that you have an online file available of a wi-fi survey, and you are going to write a script that will read this wi-fi survey and both replace an existing PDF and update a web map to show the location of wi-fi coverage.  
You will be provided with an mxd, a layer file, and part of the html file for Leaflet.  
(Note: The sample data and exam data will not be real maps of wi-fi coverage.)  


## Functions that you will write  
1. Modify a python object according to specifications and output a tuple. (Data structures)  
2. Return a timestamp from a string with a specified timezone. (datetime & pytz)  
3. Check for the presence of a shapefile in a path, and create the shapefile if needed. (arcpy)  
4. Retrieve a json array using ```requests``` from a specific url and return a list of python objects. Optionally, use ```urllib2```. (requests or urllib2)  
5. Take a shapefile and a tuple representing a feature, and insert the feature if it is not present. (arcpy.da)
6. Convert a shapefile to geojson using ```fiona```. (fiona)  
7. With ```shapely``` or ```arcpy```, buffer points in a shapefile, using a value from a field. (shapely and fiona or arcpy geoprocessing)  
8. Combine rasters using ```numpy``` and output to new raster, with ```arcpy```, not ```rasterio```, due to ```numpy``` conflict. (numpy)  
9. Generate a PDF file from an MXD based on the extent of a layer in the MXD. (arcpy.mapping)  
10. Create a webmap using geojson (Leaflet)  

## Rules
* You can use any resource you want except each other and live people (cannot text a friend, post on a forum, etc).  
* You can prepare code samples ahead of time.  
* You will be provided with intermediate outputs in case you get stuck on an earlier part of the exam.  
* Exam grading will focus on being able to get correct results from each function. Commenting is not necessary, but can help explain your logic, particularly if a function is only partially complete.  
