var colorChanged = function() {
	var ddl = document.getElementById("id_color");
	var newColor = ddl.value;
	ddl.className = "svo-" + newColor;
};

/* paged loaded */
var ddlColor = document.getElementById('id_color');
if(ddlColor.attachEvent) {
	ddlColor.attachEvent('onchange', colorChanged);	
}
else {
	ddlColor.addEventListener('change', colorChanged , false);	
}
colorChanged();


tinyMCE.init({
        theme : "modern",
        mode : "textareas",
        width: "100%",
        skin_url: DjangoURL.static + 'css/vendor/tinymce/skins/lightgray'


});