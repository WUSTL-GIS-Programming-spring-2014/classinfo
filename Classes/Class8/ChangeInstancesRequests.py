# Demonstrates how to modify the min and max instances for a service

# For Http calls
import httplib, urllib, json, requests

# For system tools
import sys

# For reading passwords without echoing
import getpass


# Defines the entry point into the script
def main(argv=None):
    # Print some info
    print
    print "This tool is a sample script that resets the minimum and maximum instances allowed for a service."
    print

    # Ask for admin/publisher user name and password
    username = raw_input("Enter user name: ")
    password = getpass.getpass("Enter password: ")
    
    # Ask for server name
    serverName = raw_input("Enter Server name: ")
    serverPort = 6080

    
    print r"Enter the service name in the format <folder>/<name>.<type>."
    service = raw_input(r"For example USA/Chicago.MapServer: ")
    minInstances = raw_input(r"Enter the minimum number of instances per node: ")
    maxInstances = raw_input(r"Enter the maximum number of instances per node: ")
    
    # Get a token
    token = getToken(username, password, serverName, serverPort)
    if token == "":
        print "Could not generate a token with the username and password provided."    
        return
    
    serviceURL = u'http://{}:{}'.format(serverName,serverPort) + "/arcgis/admin/services/" + service
    
    # This request only needs the token and the response formatting parameter 
    params = {'token': token, 'f': 'json'}
    
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    
    # Connect to service to get its current JSON definition    
    r = requests.post(serviceURL,params=params,headers=headers)
    if (r.status_code != 200):
        print "Could not read service information. http status code {}".format(r.status_code)
        return
    else:
        # Check that data returned is not an error object
        if not assertJsonSuccess(r.text):          
            print "Error when reading service information. " + str(r.text)
        else:
            print "Service information read successfully. Now changing properties..."

        # Deserialize response into Python object
        dataObj = r.json()

        # Edit desired properties of the service
        if (dataObj["minInstancesPerNode"] != minInstances or dataObj["maxInstancesPerNode"] != maxInstances):
            dataObj["minInstancesPerNode"] = minInstances
            dataObj["maxInstancesPerNode"] = maxInstances

            # Serialize back into JSON
            updatedSvcJson = json.dumps(dataObj)

            # Call the edit operation on the service. Pass in modified JSON.
            editSvcURL = serviceURL + "/edit"
            params = {'token': token, 'f': 'json', 'service': updatedSvcJson}
            r = requests.post(editSvcURL, params=params,headers=headers)
            # Read service edit response
            if (r.status_code != 200):
                print "Error while executing edit. http status code {}".format(r.status_code)
                return
            else:
                # Check that data returned is not an error object
                if not assertJsonSuccess(r.text):
                    print "Error returned while editing service" + str(r.text)        
                else:
                    print "Service edited successfully."
        else:
            print "Service already has {} minimum instances and {} maximum instances.".format(minInstances,maxInstances)


        return

# A function to generate a token given username, password and the adminURL.

def getToken(username, password, serverName, serverPort):
    # Token URL is typically http://server[:port]/arcgis/admin/generateToken
    tokenURL = "/arcgis/admin/generateToken"
    url = u'http://{}:{}'.format(serverName,serverPort) + tokenURL
    
    payload = {'username': username, 'password': password, 'client': 'requestip', 'f': 'json'}
    
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    
    # Connect to URL and post parameters
    r = requests.post(url,data=payload,headers=headers)
    # Read response
    if (r.status_code != 200):
        print "Error while fetching tokens from admin URL. Please check the URL and try again."
        print "http status code {}".format(r.status_code)
        r.close()
        return
    else:
        r.close()
        # Check that data returned is not an error object
        if not assertJsonSuccess(r.text):            
            return
        # Extract the token from it
        return r.json()[u'token']            
        

# A function that checks that the input JSON object 
#  is not an error object.
def assertJsonSuccess(data):
    obj = json.loads(data)
    if 'status' in obj and obj['status'] == "error":
        print "Error: JSON object returns an error. " + str(obj)
        return False
    else:
        return True
    
        
# Script start 
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
    pass
