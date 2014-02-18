# Your name here
# Assignment 3: Making a map series with arcpy.mapping

import arcpy

def main(mapdocument, districtlayer, districts):
    """Print new PDF for each district in list districts and return list of PDF paths."""
    pdfs = []
    df = arcpy.mapping.ListDataFrames(mapdocument)[0]
    #This is one method for handling this problem. You do not have to use this method.
    for district in districts:
        #Create query logic with string concatenation. Sample query: u'"SCHOOL_DIS" = \'BRENTWOOD\''.
        query = None
        #Create logic to build an output path, e.g. u'.\\BRENTWOOD.pdf'.
        outputpath = None
        #Create selection with arcpy.SelectLayerByAttribute_management.
        
        #Zoom to selection and clear it, using a data frame method.
        df.?
        #Clear the selection with arcpy.SelectLayerByAttribute_management.
        
        #Generate the PDF and add to the list pdfs.
        arcpy.mapping.ExportToPDF(mapdocument, outputpath)
        pdfs.append(outputpath)
    return pdfs

if __name__ == '__main__':
    # Change path to mxd as appropriate. This points to Assignment3.mxd in the current working directory.
    mxd = arcpy.mapping.MapDocument(u'.\\Assignment3.mxd')
    dl = u'SchoolDistricts'
    d = [u'BRENTWOOD', u'HANCOCK PLACE', u'BAYLESS', u'MAPLEWOOD-RICHMOND HEIGHTS', u'CLAYTON']
    pdflist = main(mxd, dl, d)
    print pdflist
