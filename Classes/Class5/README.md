# Geoprocessing
### Readings
  * [```unittest``` introduction](http://pythontesting.net/framework/unittest/unittest-introduction/)  
We will review this in class as well.  
  * [Programming ArcGIS 10.1 with Python Cookbook](http://proquest.safaribooksonline.com.libproxy.wustl.edu/book/-/9781849694445/programming-arcgis-10dot1-with-python-cookbook/toc_html?uicode=washumo)
    - [Access ArcPy modules with Python from Chapter 2](http://proquest.safaribooksonline.com.libproxy.wustl.edu/book/-/9781849694445/2dot-writing-basic-geoprocessing-scripts-with-arcpy/ch02s07_html?uicode=washumo) - Can read rest of Chapter 2 for review.  
    - [Chapter 3: Managing Map Documents and Layers](http://proquest.safaribooksonline.com.libproxy.wustl.edu/book/-/9781849694445/programming-arcgis-10dot1-with-python-cookbook/ch03_html?uicode=washumo)  
    - [Chapter 5: Automating Map Production and Printing](http://proquest.safaribooksonline.com.libproxy.wustl.edu/book/-/9781849694445/programming-arcgis-10dot1-with-python-cookbook/ch05_html?uicode=washumo)  
    - [Chapter 6: Executing Geoprocessing Tools from Scripts](http://proquest.safaribooksonline.com.libproxy.wustl.edu/book/-/9781849694445/programming-arcgis-10dot1-with-python-cookbook/ch06_html?uicode=washumo)  
    - [Scheduling batch files to run at prescribed times from Appendix A](http://proquest.safaribooksonline.com.libproxy.wustl.edu/book/-/9781849694445/adot-automating-python-scripts/apas05_html?uicode=washumo)  
    - [Rest of Appendix A](http://proquest.safaribooksonline.com.libproxy.wustl.edu/book/-/9781849694445/programming-arcgis-10dot1-with-python-cookbook/apa_html?uicode=washumo) as a reference only for above.  

You can download digital materials for Programming ArcGIS 10.1 with Python Cookbook from [Dropbox](https://www.dropbox.com/sh/17yilv6oustbgfy/Juwwvsmlra)  

We will also look at how to handling licensing and installation related functions, which are documented in the ArcGIS Desktop help starting at [CheckExtension](http://resources.arcgis.com/en/help/main/10.2/index.html#/CheckExtension/018v00000059000000/)  

### Coding style
  * The main block and importing
  * Functions and scope
  * Classes and object orientation  
    [Demo Class](https://github.com/WUSTL-GIS-Programming-spring-2014/class_five/blob/master/multithreadclass.py)  

### Licensing and ```arcpy```

#### Version and product
```
arcpy.GetInstallInfo() #Information abut installation
(main,minor,sub) = arcpy.GetInstallInfo()['Version'].split('.')
arcpy.CheckProduct(u'arcinfo')
arcpy.SetProduct(u'arcinfo')
arcpy.ProductInfo()
```

#### Extension demo
```
arcpy.CheckExtension(u'3D')
arcpy.AddZInformation_3d()
arcpy.CheckOutExtension(u'3D')
arcpy.AddZInformation_3d()
arcpy.CheckInExtension(u'3D')
arcpy.AddZInformation_3d()

```

### Geoprocessing
[Sample files on dropbox](https://www.dropbox.com/s/ewanlg0vhm9rkv7/Assignment3.zip)  
Our plan: Take only the public schools and divide them up into feature classes by school district
 1. Test for the existence of our file geodatabase using ```arcpy.Exists()```
    If absent, create with ```CreateFileGDB_management (out_folder_path, out_name, {out_version})```
 2. If the file geodatabase existed, check for existing output using ```arcpy.Exists()``` and warn user of overwrite.
 3. Create a feature class of public schools
    - Use ```arcpy.CreateScratchName()``` for our temp file name
    - Can use ```arcpy.Select_analysis()```  
      *or*  
      ```arcpy.SelectLayerByAttribute_management()``` + ```arcpy.CopyFeatures_management()```
 4. Divide the schools up by district with ```arcpy.Split_analysis()```

### Scheduled Tasks
 * Setting the path
   - Applies to *next* commend prompt
   - Why I use ```pythonw.exe myfile.py``` instead of just ```myfile.py```
 * Scheduling the task itself

### ```arcpy.mapping```

#### The 'boilerplate'
```
import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
```
Most "List" functions like ```ListDataFrames``` return Lists. (Watch for tuples though.)

#### Refreshing
 * ```arcpy.RefreshTOC()```
 * ```arcpy.RefreshActiveView()```
 * ```arcpy.RefreshCatalog()``` and why it wants an argument

#### Extents
 * ```df.extent```
 * ```arcpy.Extent``` objects
    - Layers (```arcpy.mapping.ListLayers(mxd)```)
    - Bookmarks (```arcpy.mapping.ListBookmarks(mxd)```)
    - Build your own (XMin, YMin, XMax, YMax)

#### Layout Elements
[```arcpy.mapping.ListLayoutElements()```](http://resources.arcgis.com/en/help/main/10.2/index.html#/ListLayoutElements/00s30000003w000000/])  
```
arcpy.mapping.MapsurroundElement
arcpy.mapping.GraphicElement
arcpy.mapping.PictureElement
arcpy.mapping.LegendElement
```

#### Symbology
You have to use existing .lyr files.
Can do some limited modification of [some symbology]((http://resources.arcgis.com/en/help/main/10.2/index.html#/UniqueValuesSymbology/00s30000005s000000/)):  
 * Graduated Color
 * Graduated Symbol
 * Raster Classified
 * Unique Values

#### ```arcpy.mapping.ExportTo...```
[```arcpy.mapping.ExportToPDF```](http://resources.arcgis.com/en/help/main/10.2/index.html#/ExportToPDF/00s300000027000000/) is most commonly used
```
doc = arcpy.mapping.PDFDocumentCreate(<path>)
http://resources.arcgis.com/en/help/main/10.2/index.html#/PDFDocumentCreate/00s300000019000000/
doc.appendpages(<additional doc path>)
doc.saveAndClose()
```

#### What you cannot do!
 * Cannot create an mxd!
 * Cannot create a .lyr!
 * Cannot create new date frames!
 * Cannot create new text elements!
(But can clone existing MapDocument or Layer with ```saveCCopy``` or TextElment with ```clone```.)

## Assignment 3 Links
[Assignment](https://github.com/WUSTL-GIS-Programming-spring-2014/class_five/blob/master/Assignment3.py)  
[Sample files on dropbox](https://www.dropbox.com/s/ewanlg0vhm9rkv7/Assignment3.zip)  
