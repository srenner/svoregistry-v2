var colorChanged = function() {
	var ddl = document.getElementById("id_color");
	var newColor = ddl.value;
	//document.getElementById("divColorPreview").className = "color-preview svo-" + newColor;
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
