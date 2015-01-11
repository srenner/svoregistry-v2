(function getYearData() {
	promise.get('/statistics/year').then(function(error, text, xhr) {
		if (error) {
			return;
		}
		var data = JSON.parse(text);
		alert(data);
	});
})();