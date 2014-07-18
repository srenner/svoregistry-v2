(function drawCarMap() {
	promise.get('/map/' + activeCar + '/').then(function(error, text, xhr) {
		if (error) {
			return;
		}
		var data = JSON.parse(text);
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
	        	position: new google.maps.LatLng(data[i].lat, data[i].long),
	        	desc: "<div style='min-width: 150px'><a href='#" + data[i].entry_id + "'>" + data[i].date + "</a><br>" + data[i].owner + "</div>",
	        	map: map
			});
			markers.push(marker);
			oms.addMarker(marker);
		}
    	var mapOptions = {gridSize: 30, maxZoom: 7};
    	var mc = new MarkerClusterer(map, markers, mapOptions);
	});
})();

(function initializeDatepicker() {
    var picker = new Pikaday(
    {
        field: document.getElementById('id_entry_datetime'),
        firstDay: 1,
        minDate: new Date('1983-03-02'),
        onSelect: function() {
            document.getElementById('id_entry_datetime').value = this.getMoment().format('MM/DD/YYYY');
        }
    });
    picker.setMoment(moment());
})();

