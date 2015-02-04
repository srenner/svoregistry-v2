$(document).ready(function() {
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
				//alert(data);
			}
	});
	return false;
};