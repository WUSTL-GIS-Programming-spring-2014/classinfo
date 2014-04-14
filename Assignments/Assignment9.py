# (Place your name here in a comment)
# Assignment 9: Mapping siren coverage with fiona and shapely
# Sirens shapefile available on dropbox at https://www.dropbox.com/s/6utd50wr6pvqtmv/Sirens.shp.zip
# This section of the fiona manual may be helpful: http://toblerity.org/fiona/manual.html#writing-new-files

import os
import fiona
from shapely.geometry import mapping, shape
# shapely.geometry.shape : http://toblerity.org/shapely/shapely.geometry.html#shapely.geometry.shape
# shapely.geometry.mapping: http://toblerity.org/shapely/shapely.geometry.html#shapely.geometry.mapping

def main():
    """Buffer sirens and write out a new shapefile using fiona and shapely."""
	home = u'Your root directory' # Set the root directory that you are reading from for fiona
	os.chdir(home)
	input = u'Sirens.shp' # Change to the correct relative path to your siren shapefile. You can also read from inside the zip file as a virtual filesystem instead.
	ouput = u'name of your output shapefile'
	# More information on virtual filesystems and fiona here: http://toblerity.org/fiona/manual.html#virtual-filesystems
    
	# Read in your source shapefile using fiona.open()
	
	    # Interate over your input modifying the 'geometry' property of each feature
		# And write your features back out to a new shapefile
	
	return output # Output should be a reference to the output shapefile, at minimum the name but ideally a path or other handle to it.
		

# Call your main function when program is executed.
# This allows import without executing the main function
if __name__ == '__main__':
    main()

