# Quiz 9: Open Source Mapping

###Name the javascript object format (2 pts each)  
1\. A format for encoding data structures returned from calls to the ArcGIS Server Rest API  
  *esriJSON*  
  
2\. An open source format for encoding geospatial features and their attributes, commonly used in open source web mapping  
  *geoJSON*  
  
3\. A format for encoding geospatial topology as well as features, allowing for reduced file size but not directly usable in any web mapping frameworks  
  *topoJSON*  
  
    
### True/False (2 pts each)  
4\. Conversion from EsriJSON to GeoJSON is simple for all vector types except MultiPolygons.  
  *True*  
  
5\. In Leaflet, vectors are commonly rendered as markers composed of a layer for each feature.  
  *False*  
  
6\. In Leaflet, rasters are commonly rendered as layers of tiles.  
  *True*  
  
  
  
  
###You have a simple html document that looks like this:
  
    <html>
	<head></head>
	<body>
		<p>A</p>
		<p>B</p>
		<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
		<script>
			var data = [5,10,15,20];
		</script>
	</body>
    </hmtl>

  
Describe the results of these three function calls (3 pt each)  
  
7\. d3.select("p");  
  *The first paragraph (p) element in the page, whose text is currently "A".*  
  
8\. d3.selectAll("p");  
  *An iterator of two paragraph elements, whose text is currently "A" and "B".*  
  
9\. d3.selectAll("p").data(data, function(d){return d;}).enter();  
  *In interator of the two data values 15 and 20, the two values that are not bound to paragraph elements from the selectAll.*  
  
