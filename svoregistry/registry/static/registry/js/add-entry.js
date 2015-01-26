$(document).ready(function() {
	var ddlColor = document.getElementById('id_color');
	if(ddlColor.attachEvent) {
		ddlColor.attachEvent('onchange', colorChanged);	
	}
	else {
		ddlColor.addEventListener('change', colorChanged , false);	
	}
	colorChanged();
	
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


var addEntryAjax = function() {
	if(!window.FormData) {
		return true;
	}
	//if we made it this far we can perform file upload via ajax	

	var fd = new FormData(document.getElementById("formAdd"));

	$.ajax({
		url: "/" + activeCar + "/",
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
