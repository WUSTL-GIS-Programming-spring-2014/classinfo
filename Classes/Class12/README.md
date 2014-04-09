## Advanced Development Environment

### Some guides:
[Installing Python on Windows](http://docs.python-guide.org/en/latest/starting/install/win/)  
[How to install pip on Windows](http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows)  
http://arunrocks.com/guide-to-install-python-or-pip-on-windows/

### easy_install  
####setuptools -> distribute -> setuptools  
[What is the difference?](http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2/6522905#6522905)  
  
####easy_install (part of setuptools)-> pip  
pip can uninstall  
But... easy_install works better on windows because it handles binaries.  
  
###Another option  
https://sites.google.com/site/pydatalog/python/pip-for-windows  
What does it do?  
Why use other options?  
  
###Interactive startup file  
https://docs.python.org/2/tutorial/interpreter.html#the-interactive-startup-file  
**Need to investigate why this is not working with arcpy**  
  
==========  
## [OGR](http://www.gdal.org/ogr/)  
Part of GDAL C++ library for read/write access to many spatial formats.  
GDAL = Raster  
OGR = Vector  
Think of it as a translation library that includes Includes ESRI Shapefile, ESRI ArcSDE, MapInfo (tab and mid/mif), GML, KML, PostGIS, and Oracle Spatial.  
  
Has a python package, which we will not use. Find more at [PyPI](https://pypi.python.org/pypi/GDAL/)  
  
## [fiona](http://toblerity.org/fiona/fiona.html)  
Installer at [Python Extension Packages for Windows](http://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona)  
[Base documentation](http://toblerity.org/fiona/README.html)  

fiona.open()  
[fiona.open examples](https://github.com/Toblerity/Fiona/blob/master/examples/open.py(  
len()  
next()  
fiona records  
fiona collections  
  - c.driver  
  - c.crs (proj.4 parameters with)  
  - fiona.crs.to_string, fiona.crs.from_string, fiona.crs.from_epsg  
  - c.schema  

## [shapely](http://toblerity.org/shapely/shapely.html)  
http://toblerity.org/shapely/manual.html#spatial-analysis-methods  
http://toblerity.org/shapely/manual.html#constructive-methods  


## Class Example
[ShapeToGeojson.py](https://github.com/WUSTL-GIS-Programming-spring-2014/classinfo/blob/master/Classes/Class12/ShapetoGeojson.py)  
