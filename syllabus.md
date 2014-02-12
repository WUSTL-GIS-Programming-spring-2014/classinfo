#GIS Programming
## Spring 2014

### BOOKS
*Books are accessed through [WUSTL Safari Tech Books Online](http://library.wustl.edu/subjects/engineering/safari.html)*  
**Primary**  
[Think Python](http://proquest.safaribooksonline.com.libproxy.wustl.edu/book/programming/python/9781449332006?uicode=washumo)  
[Programming ArcGIS 10.1 with Python Cookbook](http://proquest.safaribooksonline.com.libproxy.wustl.edu/book/-/9781849694445?uicode=washumo)  
[Course materials for Programming ArcGIS 10.1 with Python Cookbook posted to Dropbox](https://www.dropbox.com/sh/17yilv6oustbgfy/Juwwvsmlra)  
[Python Geospatial Development - Second Edition, Chapter 3 only](http://proquest.safaribooksonline.com.libproxy.wustl.edu/book/programming/python/9781782161523/3dot-python-libraries-for-geospatial-development/ch03_html?uicode=washumo)  
  
**Supplemental Reading**   
[Python® Programming for the Absolute Beginner (not 3rd edition)](http://proquest.safaribooksonline.com.libproxy.wustl.edu/book/programming/python/1592000738?uicode=washumo)  
[Learning Python](http://proquest.safaribooksonline.com.libproxy.wustl.edu/book/programming/python/9781449355722?uicode=washumo)  
  
  
### CLASS SCHEDULE  
  
  
1.  [**1/15/2014** Course Introduction](https://github.com/WUSTL-GIS-Programming-spring-2014/classinfo/blob/master/Class1.md)  
    *   Installation  (http://docs.python.org/2/using/windows.html)  
    *   IDLE Toying (https://hkn.eecs.berkeley.edu/~dyoo/python/idle_intro/)  
    *   Sublime (http://www.sublimetext.com/)  
        -   Package Control (https://sublime.wbond.net/ )  
    *   git (http://git-scm.com/book/en/Getting-Started-Git-Basics)  
        -   Code School tryGit (http://try.github.io/levels/1/challenges/1)  
    *   github (https://help.github.com/articles/set-up-git)  
2.  [**1/22/2014** Flow Control and Functions](https://github.com/WUSTL-GIS-Programming-spring-2014/classinfo/blob/master/Class2.md)  
    *   Quiz 1  
    *   ```while``` loop  
    *   Functions and scope  
3.  [**1/29/2014**  Python Basics](https://github.com/WUSTL-GIS-Programming-spring-2014/classinfo/blob/master/Class3.md)  
    *   Introduction to ```arcpy```  
    *   32-bit and 64-bit  
    *   More Flow Control  
    *   Data Structures  
    *   Assignment 1: Batch geoprocessing  
4.  [**2/05/2014**   Modules](https://github.com/WUSTL-GIS-Programming-spring-2014/class_four)  
    *   Quiz 2: Lists and flow control  
    *   ```os```, ```datetime```, and ```pytz``` modules  
    *   Exceptions  
    *   Classes
    *   Assignment 2: Process a folder of shapefiles  
5.  [**2/12/2014**   Geoprocessing](https://github.com/WUSTL-GIS-Programming-spring-2014/class_five)  
    *   Quiz 3  
    *   Review coding style  
    *   More on Classes  
    *   ```arcpy``` - extensions and licensing  
    *   ```arcpy.mapping```  
    *   Geoprocessing  
    *   Scheduled tasks  
    *   If we have time: ```unittest``` module  
    *   Assignment 3:  Making a map series with ```arcpy.mapping```  
        [Assignment 3 materials on Dropbox](https://www.dropbox.com/s/ewanlg0vhm9rkv7/Assignment3.zip)
6.  **2/19/2014**   Working with cursors  
    *   Quiz 4: Automating your scripts  
    *   ```arcpy.da```  
    *   Search cursor  
    *   Insert cursor  
    *   Update cursor  
    *   Assignment 4: Calculate demographics in a file geodatabase  
7.  **2/26/2014**   Working with rasters  
    *   Quiz 5: ```arcpy.da``` and tuples  
    *   ```arcpy.sa```  
    *   ```Numpy```  
    *   Assignment 5:  Calculate NVDI with ```arcpy.sa```  
8.  **3/05/2014**   ArcGIS Server  
    *   Quiz 6  
    *   Creating services  
    *   Esri REST API  
    *   ```json```, ```urllib2```, and ```requests```  
    *   Assignment 6 in class:  Scripting ArcGIS Server Administration  
    *   Quiz 7 (take home): Scripting a geocode request  
9.  **3/12/2014**   Spring Break  
10. **3/19/2014**   HTML and Esri Javascript API  
    *   Quiz 7 due  
11. **3/26/2014**   Esri Javascript API  
    *   JSAPI Continued  
    *   Github Pages  
    *   Assignment 7:  Make a mashup with the JSAPI  
12. **4/02/2014**   Open Source Mapping  
    *   Quiz 8  
    *   Leaflet  
    *   OpenLayers  
    *   d3  
    *   Assignment 8:  An open source mashup  
13. **4/09/2014**   Intro to open source geospatial libraries: vector  
    *   Quiz 9: open source mapping  
	*	Advanced development environment:  
		-	```setuptools```, ```distribute```, ```easy_install```, and ```pip```  
		-	Python Package Index  
		-	http://www.lfd.uci.edu/~gohlke/pythonlibs/  
		-	```virtualenv```  
		-	interactive startup file  
    *   OGR/```fiona```  
    *   ```shapely```  
    *   Assignment 9: Mapping siren coverage with fiona and shapely  
14. **4/16/2014**   Intro to open source geospatial libraries: raster  
    *   Quiz 10: open source geoprocessing  
    *   ```pyproj``` and Proj4  
    *   GDAL/```rasterio```  
    *   Assignment 10: Calculating NVDI with ```rasterio```  
15. **4/23/2014**   Review  
    *   Review for final  
    *   Special Topics as time allows:  
	    -    Python 3  
		-    ```six```  
		-    ```matplotlib```  
		-    ```pandas```  
		-    ```scikit-learn```  
		-    ```django```  
16. **4/30/2014**   Final Exam  

  
  
###GRADING

####Course Grade
Letter grades are determined by meeting or exceeding a minimum percentage in the course  
```
    Grade    Percent    Points    
    A+       98%        980    
    A        92%        920    
    A-       90%        900    
    B+       88%        880    
    B        82%        820    
    B-       80%        800    
    C+       78%        780    
    C        72%        720    
    C-       70%        700    
    D+       68%        680    
    D        62%        620    
    D-       60%        600    
    CR       60%        600    (For Credit/No Credit option only)
```
  
#### Scored Items and Values  
10 Assignments at 75 points each  
10 Quizzes at 15 points each  
1 Final at 100 points  
Grade is percent out of 1000 points.  
  
Quizzes will generally be three to five questions.  
All assignments except assignment 9 are written in python and due at the beginning of the next class on github.  
  
####Assignment grading  
15 pts Commenting and coding style  
15 pts Syntax (no syntax errors)  
45 pts Achieves objectives  
-5 pts per day for late assignments (per 24 hours, so penalty is -10 pts at 5pm the day after class)  

