#Intro to open source geospatial libraries: raster  
  
From last class:  
Interactive startup file  
https://docs.python.org/2/tutorial/interpreter.html#the-interactive-startup-file  
On Windows, need to add the -s option to your menu item/shortcut to open IDLE with interactive startup  
  
##Quiz 10: [open source geoprocessing](https://github.com/WUSTL-GIS-Programming-spring-2014/classinfo/blob/master/Quizzes/Quiz10.md)  

##Proj4  
[Proj4](http://trac.osgeo.org/proj/)  
[```pyproj```](https://code.google.com/p/pyproj/)  
Most documentation is at http://pyproj.googlecode.com/svn/trunk/docs/pyproj.Proj-class.html  
Often an underlying library to other libraries (fiona, rasterio, etc), so may not have to use directly.    
  
###Installation
Can use `pip` for non-Windows.
On Windows, complicated manual install because it relies on C libraries.  
Instead install as ```pyproj``` from [Windows Binaries](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyproj)  
If import says dll is missing, uninstall with ```pip uninstall pyproj``` then use binary to reinstall.  
  
###Creating proj4 projection object  
  
Use ```pyproj.Proj()``` where arguments can be:
  
*  Dictionary  
*  Keyword arguments  
*  proj4 string  

```
from pyproj import Proj  
p_dictionary = Proj({'proj':'utm', 'zone':10, 'ellps':'WGS84'})  
p_keywordarg = Proj(proj='utm',zone=10,ellps='WGS84')  
p_proj4string = Proj('+proj=utm +zone=10 +ellps=WGS84')
```
  
Can look up proj4 strings or epsg codes with http://spatialreference.org/ref/epsg/  
or with http://epsg.io/  
Can look up parameters with http://www.remotesensing.org/geotiff/proj_list/  
  
Also can use ```fiona.crs.from_espg()``` and ```fiona.crs.to_string()```
```
crs = fiona.crs.from_epsg(26996)
fiona.crs.to_string(crs)
# '+init=epsg:26996 +no_defs'
```
  
Not all projections are EPSG defined (e.g. State Plane Missouri East FIPS 2401 Feet is ESRI:102696).  
Will need to use proj4 strings for those.  
  
```p_sp_mo_e = Proj('+proj=tmerc +lat_0=35.83333333333334 +lon_0=-90.5 +k=0.9999333333333333 +x_0=250000 +y_0=0 +datum=NAD83 +units=us-ft +no_defs', preserve_units=True)```   
**NOTE: pyproj always converts to meters unless you specify ```preserve_units=True```**  
  
###Reprojection
Call to the object using long,lat and get back (x,y) as tuple.  
```
p_sp_mo_e(-90.1847, 38.6245)
# (910284.5387766103, 1016388.2525478855)
```
Use inverse flag to reverse.  
```
p_sp_mo_e(910284.5387766103, 1016388.2525478855, inverse=True)
# (-90.1847, 38.62449999999999)
```

Convert between projections with ```pyproj.transform```  
```
p = Proj('+init=epsg:26996 +no_defs') # State Plane Missouri East Meters, EPSG:26996
pyproj.transform(p_sp_mo_e,p, 910284.5387766103, 1016388.2525478855)  
# (277455.2823296753, 309795.7589681125)
```
  
###Example
Will walk through [fiona example](https://github.com/Toblerity/Fiona/blob/master/examples/with-pyproj.py) in class  
  
  
  
## GDAL  
Open source translator library for raster geospatial data.  
Tutorials are written in several languages including python.  
[GDAL Tutorial link](http://www.gdal.org/gdal_tutorial.html)  
  
## ```rasterio```  [Github repo](https://github.com/mapbox/rasterio)  
Nicer interface on GDAL from mapbox.  
  
###Installation
Requires ```numpy``` (which installs with ```arcpy```), but a higher version than arcpy 10.2  
Must install [GDAL](http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal) first. Again, needs C libraries, so use binary installer on Windows.  
Can install [rasterio](http://www.lfd.uci.edu/~gohlke/pythonlibs/#rasterio) with binary or with pip.  

###Examples  
Examples come from the [Github repo](https://github.com/mapbox/rasterio)  
Use ```os.startfile(path)``` instead of ```subprocess.open(['open',path])```  
Use ```c:\python27\arcgis10.2\python <root>\rasterio\scripts\rio_insp <file>``` instead of rasterio.insp or rio_insp  
Have to install GDAL to use ```gdalinfo```  

Assignment 10: Calculating NDVI with rasterio  

##Before we are done  
```import this```  
