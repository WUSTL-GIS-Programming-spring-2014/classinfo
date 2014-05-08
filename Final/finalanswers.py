import logging #This will allow full error traceback without breaking execution
logging.basicConfig(level=logging.ERROR)

#Place your import statements here
import requests
import datetime
import pytz
import arcpy
import fiona
import json
import numpy

def func1(url):
    """func1(url) Retrieves a javascript file containing json from url. Returns
    that json as a python object, or returns False if there is an http error."""
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return False

def func2(datestring):
    """func2(datestring) Convert string in the format yyyy/mm/dd to datetime object at midnight CST on that date."""
    #The string for Central Time Zone is "US/Central"
    y,m,d = datestring.split("/")
    ts = datetime.datetime(int(y),int(m),int(d))
    central = pytz.timezone("US/Central")
    return central.localize(ts)

def func3(site):
    """func3(site) Wifi site dictionary is returned as a tuple reformatted according to a specification."""
    #Specification:
    #   first element of the tuple is the 'site' id unmodified
    #   second element of the tuple is 'building' with all words capitalized and no extra whitespace
    #   third element of the tuple is a tuple of ('long','lat')
    #   fourth element of the tuple is 'type' unmodified
    #   fifth element of the tuple is the integer range returned from 'type' using the function getRange()
    return (site['site'],site['building'].title().strip(),(site['long'],site['lat']),site['type'],getRange(site['type']))

def func4(path,shp):
    """func4(path,shp) Verifies shapefile shp exists at path.
    If it does not exist, create a point shapefile using the fields and spatial reference given.
    Returns the full path (e.g. u'C:\\final\\exam.shp') to the shapefile."""
    fields = [
        {'field_name':'siteid','field_type':'TEXT'},
        {'field_name':'building','field_type':'TEXT'},
        {'field_name':'wifitype','field_type':'TEXT'},
        {'field_name':'range','field_type':'LONG'}]
    sr = arcpy.SpatialReference(4326) #WGS 1984 spatial reference
    #Note, make sure that the folder C:\final does exist and you have installed
    #the final exam materials in that folder
    #function4.shp in the ExpectedOutput folder shows what your result should be at the end of function 4
    if not arcpy.Exists(path + shp):
        arcpy.CreateFeatureclass_management(path,shp,"POINT",spatial_reference=sr)
        for field in fields:
            arcpy.AddField_management(in_table=path+shp, **field)
    return path + shp

def func5(feature,shp):
    """func5(feature,shp) searches shapefile shp for feature, represented as a tuple.
    If feature with that siteid does not exist in shp, it is inserted into the shapefile.
    Returns True if a new feature is inserted, otherwise returns false."""
    #tuple is (siteid,building,(long,lat),wifi type,range in feet) as returned from func3
    #The input shapefile should have fields siteid, building, wifitype, and range
    #Make sure that you remember to write out the feature shape too!
    #You can use the utility function getCursorLength(cursor) to get the length of a cursor
    #function5.shp contains the expected output from this function

    #This snippet is an example that should print the current number of features in shp
    #You do not have to keep it in your function
    with arcpy.da.SearchCursor(shp,['*']) as cursor:
        print "Length: " + str(getCursorLength(cursor))

    fields = ['siteid','building','SHAPE@XY','wifitype','range']
    with arcpy.da.SearchCursor(shp,['siteid'],"\"siteid\" = '{}'".format(feature[0])) as cursor:
        if getCursorLength(cursor) == 0:
            with arcpy.da.InsertCursor(shp,fields) as icursor:
                icursor.insertRow(feature)

def func6(path,shp,output):
    """func6(shp,geojson) Write shapefile shp to geojson file output in the same folder. No return value."""
    #The path will be a full path, so you do not need to set a home directory with os
    #You do not have to write out a .crs file for the geojson, but can if you want
    #output will be in the format of "name.json" and shp in the format "name.shp"
    features = []
    crsout = output.replace('.json','.crs')
    with fiona.open(path+shp) as source: #"r" mode is default.
        for feature in source:
            features.append(feature)
        crs = " ".join("+%s=%s" % (k,v) for k,v in source.crs.items())

    #Make geojson with link to crs file
    fc = {"type": "FeatureCollection",
          "features": features,
          "crs": {
              "type": "link",
              "properties": {"href": crsout, "type": "proj4"}
            }
          }
    #Write out geojson
    with open(path+output, "w") as f:
        f.write(json.dumps(fc))
    #Write out crs file
    with open(path+crsout, "w") as f:
        f.write(crs)

def func7(shp,output,field):
    """func7(shp,output,field) Buffer shapefile shp and write to output. Use distance specified in field for each feature. Return the output shapefile path."""
    #Note: This function will use a reprojected input file already created for you.
    arcpy.Buffer_analysis(shp,output,field)
    return output

def func8(wifi,campus):
    """func8(wifi,campus,output) Overlay the wifi coverage raster over the campus raster and return as a numpy uint8 array."""
    #wifi is a single band raster. Add its value to the red band
    #only of campus. Output will be three band RGB as a numpy array
    #When you create your numpy arrays, remember to turn them
    #into numpy.uint16 arrays so you can hold values greater than 256!
    wifi = arcpy.RasterToNumPyArray(wifi)
    campus = arcpy.RasterToNumPyArray(campus)
    #Original version
    overlay = (wifi.astype(numpy.uint16) + campus[0].astype(numpy.uint16))/2
    #Fancier version
    overlay = campus[0].astype(numpy.uint16) + (wifi == 255)*((wifi.astype(numpy.uint16) - campus[0].astype(numpy.uint16))/2)
    campus + wifi > campus * (wifi-campus)/2
    campus[0] = overlay.astype(numpy.uint8)
    return campus

def func9(mxd,layername,output):
    """func9(mxd,layername,output) Zoom map document mxd to the extent of layer layername as string.
    Export to PDF using output path, and return the output path."""
    mxd = arcpy.mapping.MapDocument(mxd)
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    layer = arcpy.mapping.ListLayers(mxd, layername, df)[0]
    df.extent = layer.getExtent()
    arcpy.mapping.ExportToPDF(mxd, output)
    return output
    
###################################################
#
#   For problem 10, complete the skeleton Leaflet page so
#   that you can display of map of wifi locations based
#   on the geojson file you put earlier.
# 
###################################################
    

###################################################
# 
#Functions below here are utility functions that you will use in your program
def getCursorLength(cursor):
    cursor.reset()
    size = sum(1 for i in cursor)
    cursor.reset()
    return size
def getRange(wifitype):
    """wifitype -> single character string of wifitype. Returns range in feet as integer."""
    wifitypes = dict([('A',100),('B',200),('G',250),('N',300)])
    return wifitypes[wifitype]
                                           
###################################################
# 
#Functions below here are object providers that will help you continue if your program does not work correctly
def getSites():
    return [{u'building': u'Rudolph Hall      ', u'locatorrow': u'6', u'site': u'A-00007', u'long': -90.30445, u'blgnumber': u'095', u'lat': 38.64908, u'type': u'B', u'locatorcolumn': u'J'}, {u'building': u'Compton Hall      ', u'locatorrow': u'6', u'site': u'A-00003', u'long': -90.3051, u'blgnumber': u'023', u'lat': 38.64934, u'type': u'G', u'locatorcolumn': u'J'}, {u'building': u'Crow Hall         ', u'locatorrow': u'6', u'site': u'A-00006', u'long': -90.30526, u'blgnumber': u'024', u'lat': 38.649, u'type': u'N', u'locatorcolumn': u'J'}, {u'building': u'Whitaker Hall     ', u'locatorrow': u'6', u'site': u'A-00002', u'long': -90.3032, u'blgnumber': u'125', u'lat': 38.64908, u'type': u'A', u'locatorcolumn': u'K'}, {u'building': u'Brookings Hall    ', u'locatorrow': u'7', u'site': u'A-00001', u'long': -90.30502, u'blgnumber': u'015', u'lat': 38.64804, u'type': u'G', u'locatorcolumn': u'J'}, {u'building': u'Beaumont Pavillion', u'locatorrow': u'6', u'site': u'A-00004', u'long': -90.30551, u'blgnumber': u'010', u'lat': 38.64848, u'type': u'B', u'locatorcolumn': u'I'}]
def getSitesTuple():
    return [(u'A-00007', u'Rudolph Hall', (-90.30445, 38.64908), u'B', 200), (u'A-00003', u'Compton Hall', (-90.3051, 38.64934), u'G', 250), (u'A-00006', u'Crow Hall', (-90.30526, 38.649), u'N', 300), (u'A-00002', u'Whitaker Hall', (-90.3032, 38.64908), u'A', 100), (u'A-00001', u'Brookings Hall', (-90.30502, 38.64804), u'G', 250), (u'A-00004', u'Beaumont Pavillion', (-90.30551, 38.64848), u'B', 200)]
###################################################
# 
# This is the main() function. Do not modify it.
def main():
    #Do not modify main().
    #main() will automatically provide arguments for later functions if an earlier function fails.
    global step
    global sites
    arcpy.env.overwriteOutput = True
    step = [0,0,0,0,0,0,0,0,0]
    try:
        url = u'https://raw.githubusercontent.com/WUSTL-GIS-Programming-spring-2014/classinfo/master/Final/sample.js'
        sites = func1(url)
        assert sites == getSites()
        print "Function1 executed correctly."
        step[0] = 1
    except AssertionError as ex:
        logging.exception("Function 1 output is not correct")
    except Exception as ex:
        logging.exception("Error in Function 1")
    try:
        #Testing function 2 to verify that correct date string is returned
        assert str(func2('2014/04/01')) == '2014-04-01 00:00:00-05:00'
        assert str(func2('2012/01/01')) == '2012-01-01 00:00:00-06:00'
        print "Function2 executed correctly."
        step[1] = 1
    except Exception as ex:
        logging.exception("Error in Function 2")
    try:
        if step[0] == 0:
            sites = getSites()
        sites = map(func3,sites) #Runs each item in sites through func3
        assert sites == getSitesTuple()
        print "Function3 executed correctly."
        step[2] = 1
    except AssertionError as ex:
        logging.exception("Function 3 output is not correct")
    except Exception as e:
        logging.exception("Error in Function 3")
    try:
        path = u'C:\\final\\'
        shp = u'exam.shp'
        path5 = func4(path,shp)
        assert arcpy.Exists(path5)
        print "Function4 appears to have executed correctly.\nCompare exam.shp fields to function4.shp to verify."
        step[3] = 1
    except AssertionError as ex:
        logging.exception("exam.shp was not created by Function 4. Continuing with cont4.shp.")
    except Exception as e:
        logging.exception("Error in Function 4. Continuing with cont4.shp.")
    try:
        if step[2] == 0:
            sites = getSitesTuple()
        if step[3] == 0:
            path5 = u'C:\\final\\inputs\\cont4.shp' 
        for feature in sites:
            func5(feature,path5)
        print "Function5 appears to have executed correctly.\nCompare {} to function5.shp to verify.".format(path5)
        step[4] = 1
    except Exception as e:
        logging.exception("Error in Function 5. Continuing with cont5.shp.")
    try:
        if step[4] == 0:
            shp = u'cont5.shp' #Otherwise, shp is still equal to 'exam.shp'
        func6('C:\\final\\',shp,'exam.json')
        print "Function6 appears to have executed correctly.\nCompare exam.json to function6.json to verify."
        step[5] = 1
    except Exception as e:
        logging.exception("Error in Function 6.")
    try:
        shp = u'C:\\final\\inputs\\start7.shp'
        output = u'C:\\final\\end7.shp'
        field = 'range'
        func7(shp,output,field)
        print "Function7 appears to have executed correctly.\nCompare end7.shp to function7.shp to verify."
        step[6] = 1
    except Exception as e:
        logging.exception("Error in Function 7.")
    try:
        #Single band image showing existence of wifi coverage
        wifi = u'C:\\final\\inputs\\wifi.tif'
        #Three band RGB color image of WUSTL campus
        wustl = u'C:\\final\inputs\\wustl.tif'
        overlay = func8(wifi,wustl)
        #Set the spatial reference system for output so that output will have a spatial reference
        arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(102696)
        kwargs = {'lower_left_corner': arcpy.Point(874344.449318, 1024085.01983),
                  'x_cell_size': 0.49212499999947473,
                  'y_cell_size': 0.4921249999994818}
        output = arcpy.NumPyArrayToRaster(overlay.astype(numpy.uint8), **kwargs)
        output.save(u'C:\\final\\overlay.tif')
        print "Function8 appears to have executed correctly.\nCompare overlay.tif to function8.tif to verify."
        step[7] = 1
    except Exception as e:
        logging.exception("Error in Function 8.")
    try:
        mxd = u'C:\\final\\inputs\\Function9.mxd'
        layername = u'function7'
        output = u'C:\\final\\coverage.pdf'
        func9(mxd,layername,output)
        print "Function9 appears to have executed correctly.\nCompare coverage.pdf to function9.pdf to verify."
        step[8] = 1
    except Exception as e:
        logging.exception("Error in Function 9.")
    
        
    
    
if __name__ == '__main__':
    main()
    
