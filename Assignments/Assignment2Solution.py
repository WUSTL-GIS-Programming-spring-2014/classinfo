# Your name here
# Assignment 2: Process a folder of shapefiles
# Using the os library, find all shapefiles,and only shapefiles in a given folder and buffer them as before.
# Catch exceptions to handle invalid shapefiles.
import arcpy
import os

def main(inputfolder,prefix,outputfolder):
    """Buffer all shapefiles in inputfolder, appending with prefix and output to outputfolder."""
    filelist = os.listdir(inf)
    for f in filelist:
        if f.endswith('.shp'):
            try:
                input = inputfolder + f
                output = outputfolder + prefix + f
                arcpy.Buffer_analysis (input, output, u'500 Feet')
            except Exception as e:
                print "Unable to buffer", f
                print e
    return outputfolder

if __name__ == '__main__':
    # Arguments must be supplied in the __main__ block, not in the function called.
    inf = u'C:\\Facilities\\'
    p = u'Buffered_'
    outf = u'C:\\Facilities\\'
    # Print output location to standard output
    print "Output written to", main(inf, p, outf)
