import os
import fiona
from shapely.geometry import mapping, shape
from json import dumps


home = u'D://' #root drive you are reading from
shp = u'arcgis//SirenBuffers.shp' #source shapefile, referenced from root
outpath = u'Scripts//' #directory you are writing too
outlyr = 'SirenBuffers' #name of the geojson file you will write to, will write both outlyr.json and outlyr.crs (coordinate reference system)

os.chdir(home) #Fiona relies on relative references to home, so changing here to the drive I am reading from.

#Use fiona to create array of features from shapefile and create crs to write
features = []
with fiona.open(shp) as source: #"r" mode is default.
    for feature in source:
        #Buffer distnace is based on crs of feature
        feature['geometry'] = mapping(shape(feature['geometry']).buffer(100.0)) #Treating fiona feature geometry as shapely shape, buffer 0 to fix invalid geometry and map back to geojson
        features.append(feature)
    crs = " ".join("+%s=%s" % (k,v) for k,v in source.crs.items())

#Make geojson with link to crs file
fc = {"type": "FeatureCollection",
      "features": features,
      "crs": {
          "type": "link",
          "properties": {"href": outlyr + '.crs', "type": "proj4"}
        }
      }
#Write out geojson
with open(outpath + outlyr + '.json', "w") as f:
    f.write(dumps(fc))
#Write out crs file
with open(outpath + outlyr + '.crs', "w") as f:
    f.write(crs)
