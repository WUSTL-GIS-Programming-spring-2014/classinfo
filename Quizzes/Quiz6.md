1. What command is necessary before using ```arcpy.sa``` functions? (3pt)  
  
    **arcpy.CheckOutExtension**  
    arcpy.CheckProduct  
    arcpy.CheckExtension  
  
2. Briefly explain what has likely gone wrong if you encounter a ```MemoryError``` while using a ```numpy``` array and how you might fix that issue.(4pt)  
  
    *The size of the array has exceeded the memory available to the python process. This is particularly likely to happen if you are using 32-bit python and using a float array.*  
    *You can fix this issue by using 64-bit python or by converting the array to an integer array, if this can be done without loss of precision.*  
  
3. What is the primary purpose of the classes in ```arcpy.sa```, such as ```arcpy.sa.NbrCircle```? (4pt)  
  
  *The ```arcpy.sa``` classes primiarly provide specialized argument classes for Spatial Analyst tools.*
  
4. If you have an image that has 6 bands and is 8192 pixels wide and 8192 pixels high, what are the dimensions of the numpy array produced from it? (4pt)   
Answer should be in the form of ```[][][]```  
  
  *[6][8192][8192]*
