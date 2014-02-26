# Working with Rasters
*Install [scipy‑0.13.3.win32‑py2.7.exe](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy)*

## Readings
  * [An introduction to Numpy and Scipy](http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf)
  * [An overview of the Map Algebra Operators (arcpy.sa)](http://resources.arcgis.com/en/help/main/10.1/index.html#/An_overview_of_the_Map_Algebra_Operators/005m000000mm000000/)
  * [Review Neighborhood Statistics from Spatial Analyst](http://resources.arcgis.com/en/help/main/10.1/index.html#/An_overview_of_the_Neighborhood_tools/009z000000qn000000/)  
    Particularly look at Focal Statistics, as we will use this in class  
## Supplemental Reading
  * [Tenative NumPy Tutorial](http://wiki.scipy.org/Tentative_NumPy_Tutorial)
  * [arcpy.sa Neigborhood classes](http://resources.arcgis.com/en/help/main/10.1/index.html#/An_overview_of_neighborhood_classes/005m0000001p000000/)  
    Neighborhood classes will make much more sense after class
    
## Map Algebra  
  * Convert DEM between meters and feed (3.28 feet per meter)  
  * Rescale DEM  
  
## Map Algebra with numpy
  * RasterToNumPyArray  
  * NumPyArrayToRaster  

## Using ```arcpy.sa```
  * ```arcpy.sa``` objects
  * neighborhood classes
  * Density smoothing with focal statistics.  
  
## Edge detection with Scikit-image  
See more examples at the [skimage gallery](http://scikit-image.org/docs/dev/auto_examples/)  
