(function handleFlag()
{
	var anchors = document.getElementsByClassName('flag-entry');
	for(var i = 0; i < anchors.length; i++) {
		anchors[i].onclick = function() {
			var entryID = this.getAttribute('data-entry-id');
			var that = this;
			$.post('/flag/' + entryID + '/', function(data) {
				that.innerHTML = 'Thank you for your feedback';
			});
		};
	}
})();