# Quiz 7
For this quiz, you will have to create a python script that will geocode addresses.  
To get full credit for the quiz, using this list:  

    addresses = [("41 S Central Ave, Clayton, Missouri, 63105","St Louis County Administration Building"),
    ("1 Brookings Dr, Saint Louis, Missouri, 63130","Washington University in St Louis"),
    ("200 Washington Ave, Saint Louis, Missouri, 63102","Gateway Arch"),
    ("901 N Broadway, Saint Louis, Missouri, 63102","Edward Jones Dome"),
    ("10701 Lambert International Blvd, Saint Louis, Missouri, 63145","Lambert-St Louis International Airport"),
    ("15193 Olive Blvd, Chesterfield, Missouri, 63017", "The Butterfly House")]
  
You must geocode the addresses for the six locations and write out a point feature class to a file geodatabase that has a minimum of two fields:
  1. "Address": Contains the original address.  
  2. "Name": Contains the name of the location.  
  
The file geodatabase feature class may be created ahead of time if you want.  
  
To do your geocoding, use this service:  
http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find  
It requires two parameters:  
```text``` The single line address. Each address above should get a 100% match.  
```f``` The format. For this service, this *must* be set to json. The service will not allow html queries.  

You can find additional help for this service at [ArcGIS REST API - World Geocoding Service - Single input field geocoding](http://resources.arcgis.com/en/help/arcgis-rest-api/#/Single_input_field_geocoding/02r300000015000000/)  

You can use ```requests``` or ```urllib2``` to make your http connections. This would probably be easy with a Session object from ```requests```.  Remember to install the ```requests``` library if you plan to use it, with your best install option probably being the [Unofficial Windows Binaries for Python Extension Packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/#requests)  
  
  
If you would like an extra challenge, you can try these alternatives (but please submit the quiz first as assigned).  
###Input  
  * Read the addresses from the provided csv file, [addresses.csv](https://raw.github.com/WUSTL-GIS-Programming-spring-2014/classinfo/master/Quizzes/Quiz7/addresses.csv).  
  * Read the address from the provided json file, [addresses.json](https://raw.github.com/WUSTL-GIS-Programming-spring-2014/classinfo/master/Quizzes/Quiz7/addresses.json).  
  
###Output  
  * Create the feature class you are writing the addresses out to as part of the script.  
  * Write the feature class out to a file in esrijson format. 
  
Hint:  
  
    desc = arcpy.Describe(FeatureSet)
    print desc.json
  
For a particular difficult challenge, try to write the feature class out to a file in [GeoJSON format](http://geojson.org/).  Even with just point features, this is not trivial.  
