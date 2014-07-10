(function handleFlag()
{
	var anchors = document.getElementsByClassName("flag-entry");
	for(var i = 0; i < anchors.length; i++) {
		anchors[i].onclick = function() {
			var entryID = this.getAttribute("data-entry-id");
			
			alert(entryID);
			//promise.post(url, data, headers)
		};
	}
})();