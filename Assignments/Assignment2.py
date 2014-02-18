# Your name here
# Assignment 2: Process a folder of shapefiles
# Using the os library, find all shapefiles,and only shapefiles in a given folder and buffer them as before.
# Catch exceptions to handle invalid shapefiles.
import arcpy
import os

def main(inputfolder,prefix,outputfolder):
    """Buffer all shapefiles in inputfolder, appending with prefix and output to outputfolder."""
    return outputfolder

if __name__ == '__main__':
    # Arguments must be supplied in the __main__ block, not in the function called.
    inf = u'<path to input>'
    p = u'<prefix>'
    outf = u'<path to output>'
    # Print output location to standard output
    print "Output written to", main(inf, p, outf)
