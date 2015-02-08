$(document).ready(function() {
	document.getElementById("divEntry").style.display = "none";
	document.getElementById("btnShowForm").style.display = "";
    document.getElementById("divMap").style.display = "block";
    initializeDatepicker();
	refreshWidgets();
    $('#btnShowForm').click(showAddEntry);
    $("#btnCancel").click(hideAddEntry);
    
	$('#id_color').change(colorChanged);
	colorChanged();

	$('#id_year').change(yearChanged);
	yearChanged();
	
	tinyMCE.init({
	    selector: "textarea",
	    toolbar: "bold italic bullist",
		menubar: false,
		statusbar: false,
		height: 150,
		skin_url: DjangoURL.static + 'registry/css/vendor/tinymce/skins/lightgray',
	});	
});

var refreshCar = function() {
	$.get('/refresh/' + activeCar + '/', function(data) {
		$('#header-car').html(data.header);
		$('#div-metadata').html(data.metadata);
	});
};

var refreshWidgets = function() {
	$.get('/entries/' + activeCar + '/', function(data) {
		if(data) {
			if(data.length > 1) {
				drawTimeline(data);
			}
			var mapData = [];
			for(var i = 0; i < data.length; i++) {
				if(data[i].lat) {
					mapData.push(data[i]);
				}				
			}
			if(mapData) {
				drawCarMap(mapData);
			}
		}
	});
};

var drawTimeline = function(data) {
	var container = document.getElementById('divTimeline');
	container.innerHTML = "";
	var dataCollection = [];
	for(var i = 0; i < data.length; i++) {
		var entry = {
			id: data[i].entry_id,
			content: data[i].owner + "<br>" + data[i].location + "<br><a href=#" + data[i].entry_id + ">" + data[i].date + "</a>",
			start: data[i].dateformat
		};
		dataCollection.push(entry);
	}
	var dataset = new vis.DataSet(dataCollection);
	var options = {
		min: new Date('1983', '01', '01'),
		max: new Date(),
	    editable: false, 
	    margin: {
	        item: 20
		},
		clickToUse: true
	};
	var timeline = new vis.Timeline(container, dataset, options);
};

var hideAddEntry = function() {
	document.getElementById('divEntry').style.display = 'none';
};

var showAddEntry = function() {
	document.getElementById('divEntry').style.display = '';
};

var drawCarMap = function(data) {
	var map = new google.maps.Map(document.getElementById('divMap'), {
		zoom: 3,
		scrollwheel: false,
		center: new google.maps.LatLng(39.0997, -94.5783),
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
};

var initializeDatepicker = function() {
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
};

var colorChanged = function() {
	var ddl = document.getElementById("id_color");
	var newColor = ddl.value;
	ddl.className = "svo-" + newColor;
};

var yearChanged = function() {
	var ddlColor = $('#id_color');
	var selectedColor = ddlColor.val();
	ddlColor.empty();
	var colorOptions = svoColorChoices($('#id_year').val());
	for(var i = 0; i < colorOptions.length; i++) {
		ddlColor
			.append($("<option></option>")
			.attr("value", colorOptions[i].code)
			.text(colorOptions[i].descr));
		ddlColor.val(selectedColor);
	}
	if(!ddlColor.val()) {
		ddlColor.val(colorOptions[0].code);
		colorChanged();
	}
};

var addEntryAjax = function() {
	tinyMCE.triggerSave();
	document.getElementById('id_mileage').value = document.getElementById('id_mileage').value.replace(",", "");
	if(!window.FormData) {
		return true;
	}
	//if we made it this far we can perform file upload via ajax	
	var fd = new FormData(document.getElementById("formAdd"));
	$.ajax({
		url: "/add",
		data: fd,
		processData: false,
		contentType: false,
		type: 'POST',	  
		success: 
			function(data) {
				hideAddEntry();
				var divEntries = document.getElementById("divEntries");
				if(divEntries) {
					var newEntry = document.createElement("div");
					newEntry.innerHTML = data;
					divEntries.insertBefore(newEntry, divEntries.firstChild);
				}
				refreshCar();
				refreshWidgets();				
			}
	});
	return false;
};