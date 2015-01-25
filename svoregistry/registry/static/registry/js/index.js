$(document).ready(function() {
    document.getElementById("divMap").style.display = "block";
    drawMap();
    
    $("#btnAddNo").click(function() { hideAddCar(); });
    $("#btnAddYes").click(function() { addCar(); });    
});

var drawMap = function() {
	$.get('/map/', function(data) {
		var map = new google.maps.Map(document.getElementById('divMap'), {
			zoom: 4,
			scrollwheel: false,
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
};

var lookupVin = function() {
	hideAddCar();
	var vin = document.getElementById("txtVIN").value;
	
	$.get('/validate/' + vin, function(data) {
		
		if(data.valid) {
			$.get('/lookup?vin=' + vin, function(data) {
				if(data === "1") {
					window.location = '/' + vin + '/';
				}
				else {
					document.getElementById("divAddCar").className = "show";
				}
			});				
		}
		else {
			$("#formLookup").effect("shake", { times:8, distance: 6, direction: 'left' }, 400);
		}
		
	
	});
	

	return false;
};

var hideAddCar = function() {
	document.getElementById("divAddCar").className = "hidden";
};

var addCar = function() {
	var vin = document.getElementById("txtVIN").value;
	$.post('/' + vin + '/', function(data) {
		//server should redirect but set window here if it doesn't
		window.location = '/' + vin + '/';
	});
};