#Quiz7: Geocode addresses using a rest endpoint
import arcpy
import json
import requests



def geocodeAddress(address):
    """Geocodes a single line address using the Esri World Geocode Service"""
    serviceURL = u'http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find'
    # This request only needs the single line address as text and the response formatting parameter .
    params = {'text': address, 'f': 'json'}
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    
    # Connect to service to get its current JSON definition.
    r = requests.post(serviceURL,params=params,headers=headers)
    if (r.status_code != 200):
        print "Could not geocode address {}.\r\nhttp status code {}.".format(address,r.status_code)
        return
    else:
        # Check that data returned is not an error object.
        if not assertJsonSuccess(r.text):          
            print "Error when reading service information. " + str(r.text)
        else:
            print "Address geocoded. Creating geometry."

        # Deserialize response into Python object.
        candidates = r.json()
        #Get the first returned location.
        candidate = candidates['locations'][0]
        # Create (X,Y) tuple.
        pt = (candidate['feature']['geometry']['x'],candidate['feature']['geometry']['y'])
        print "{} located at {}".format(address, pt)
        return pt

# A function that checks that the input JSON object is not an error object.
def assertJsonSuccess(data):
    obj = json.loads(data)
    if 'status' in obj and obj['status'] == "error":
        print "Error: JSON object returns an error. " + str(obj)
        return False
    else:
        return True
    
        
# Script start 
if __name__ == "__main__":
    addresses = [("41 S Central Ave, Clayton, Missouri, 63105","St Louis County Administration Building"),
                 ("1 Brookings Dr, Saint Louis, Missouri, 63130","Washington University in St Louis"),
                 ("200 Washington Ave, Saint Louis, Missouri, 63102","Gateway Arch"),
                 ("901 N Broadway, Saint Louis, Missouri, 63102","Edward Jones Dome"),
                 ("10701 Lambert International Blvd, Saint Louis, Missouri, 63145","Lambert-St Louis International Airport"),
                 ("15193 Olive Blvd, Chesterfield, Missouri, 63017", "The Butterfly House")]
    rows = []
    for address in addresses:
        #Note that locations returned are in WGS84
        location = geocodeAddress(address[0])
        rows.append(address + (location,))
    #Assumes that a WGS84 feature class named Quiz7 with fields Address and Name already exists.
    cursor = arcpy.da.InsertCursor(u'D:\\ArcGIS\\Default.gdb\\Quiz7',(u'Address',u'Name',u'SHAPE@XY'))
    #Insert each row created above into the cursor.
    try:
        for row in rows:
            cursor.insertRow(row)
    except:
        pass
    finally:
        del cursor
