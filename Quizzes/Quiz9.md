# Quiz 9: Open Source Mapping

###Name the javascript object format (2 pts each)  
1\. A format for encoding data structures returned from calls to the ArcGIS Server Rest API  
  
2\. An open source format for encoding geospatial features and their attributes, commonly used in open source web mapping  
  
3\. A format for encoding geospatial topology as well as features, allowing for reduced file size but not directly usable in any web mapping frameworks  
  
    
### True/False (2 pts each)  
4\. Conversion from EsriJSON to GeoJSON is simple for all vector types except MultiPolygons.  
  
5\. In Leaflet, vectors are commonly rendered as markers composed of a layer for each feature.  
  
6\. In Leaflet, rasters are commonly rendered as layers of tiles.  
  
  
  
  
  
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

  
Describe the results of these three function calls (3 pts each)  
  
7\. d3.select("p");  
  
8\. d3.selectAll("p");  
  
9\. d3.selectAll("p").data(data, function(d){return d;}).enter();  
  
