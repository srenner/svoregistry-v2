(function drawMap() {
	promise.get('/map/').then(function(error, text, xhr) {
		if (error) {
			return;
		}
		var data = JSON.parse(text);
		var map = new google.maps.Map(document.getElementById('divMap'), {
			zoom: 4,
			center: new google.maps.LatLng(40.5, -98.4160),
			mapTypeId: google.maps.MapTypeId.ROADMAP
		});
    	var infowindow = new google.maps.InfoWindow();
    	var oms = new OverlappingMarkerSpiderfier(map, { keepSpiderfied: true });
		oms.addListener('click', function(marker) {
			infowindow.setContent(marker.desc);
			infowindow.open(map, marker);
		});
		oms.addListener('spiderfy', function(markers) {
			infowindow.close();
		});
		var markers = [];
		for (var i = 0; i < data.length; i++) {
			var marker = new google.maps.Marker({
	        	position: new google.maps.LatLng(data[i].lt, data[i].lg),
	        	desc: "<a href='/" + data[i].v + "/'>" + data[i].v + "</a><br>" + data[i].dt + "<br>" + data[i].de + "<br>" + data[i].o,
	        	map: map
			});
			markers.push(marker);
			oms.addMarker(marker);
		}
    	var mapOptions = {gridSize: 30, maxZoom: 7};
    	var mc = new MarkerClusterer(map, markers, mapOptions);
	});
})();

$(document).ready(function() {
	$('#divStart').animate({backgroundColor:"orange"},  5000);
	$('#divStart').animate({backgroundColor:"white" },  6000);
	//document.getElementById("divStart").className = 'svo-2A';
});
