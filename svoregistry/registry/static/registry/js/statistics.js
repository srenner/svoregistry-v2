(function getColorData() {
	$.get('/statistics/color', function(data) {
		var labels = [];
		var cars = [];
		for(var i = 0; i < data.length; i++) {
			labels.push(data[i].color);
			cars.push(data[i].count);
		}
		new Chartist.Bar('#stats-color', 
		{
			labels: labels,
		  	series: [cars]
		}, 
		{
			axisX: 
		  	{
		  	},
		  	axisY: 
		  	{
		  	}
		});
	});
})();

(function getYearData() {
	$.get('/statistics/year', function(data) {
		var labels = [];
		var cars = [];
		var totals = [];
		for(var i = 0; i < data.length; i++) {
			labels.push(data[i].year);
			cars.push(data[i].count);
			totals.push(data[i].total_production);
		}
		new Chartist.Bar('#stats-year', 
		{
			labels: labels,
		  	series: [cars, totals]
		}, 
		{
			axisX: 
		  	{
		  	},
		  	axisY: 
		  	{
		  	}
		});		
	});
})();

(function getStatisticsData() {
	$.get('/statistics/status', function(data) {
		var labels = [];
		var cars = [];
		var totals = [];
		for(var i = 0; i < data.length; i++) {
			labels.push(data[i].status);
			cars.push(data[i].count);
		}
		new Chartist.Bar('#stats-status', 
		{
			labels: labels,
		  	series: [cars]
		}, 
		{
			axisX: 
		  	{
		  	},
		  	axisY: 
		  	{
		  	}
		});		
	});	
})();

(function getTimelineData() {
	$.get('/statistics/timeline', function(data) {
		var labels = [];
		var cars = [];
		var totals = [];
		for(var i = 0; i < data.length; i++) {
			labels.push(data[i].entry_year);
			cars.push(data[i].count);
		}
		new Chartist.Bar('#stats-timeline', 
		{
			labels: labels,
		  	series: [cars]
		}, 
		{
			axisX: 
		  	{
		  	},
		  	axisY: 
		  	{
		  	}
		});		
	});	
})();
