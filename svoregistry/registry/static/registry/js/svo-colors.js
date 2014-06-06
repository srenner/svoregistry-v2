var svoColorChoices = function(year) {
	var colors = [];
	switch(year) {
		case '1984':
			colors.push({code: '1C', descr: '1C Black'});
			colors.push({code: '1E', descr: '1E Silver Metallic'});
			colors.push({code: '2A', descr: '2A Medium Canyon Red'});
			colors.push({code: '9W', descr: '9W Dark Charcoal Metallic'});
		break;
		case '1985':
			colors.push({code: '1B', descr: '1B Medium Charcoal Metallic'});
			colors.push({code: '1C', descr: '1C Black'});
			colors.push({code: '1E', descr: '1E Silver Metallic'});
			colors.push({code: '2A', descr: '2A Medium Canyon Red'});
			colors.push({code: '2R', descr: '2R Jalepeno Red'});
			colors.push({code: '4E', descr: '4E Dark Sage'});
			colors.push({code: '9L', descr: '9L Oxford White'});
		break;
		case '1985.5':
			colors.push({code: '1B', descr: '1B Medium Charcoal Metallic'});
			colors.push({code: '1C', descr: '1C Black'});
			colors.push({code: '1E', descr: '1E Silver Metallic'});
			colors.push({code: '2A', descr: '2A Medium Canyon Red'});
			colors.push({code: '2R', descr: '2R Jalepeno Red'});
			colors.push({code: '4E', descr: '4E Dark Sage'});
			colors.push({code: '9L', descr: '9L Oxford White'});		
		break;
		case '1986':
			colors.push({code: '1C', descr: '1C Black'});
			colors.push({code: '1D', descr: '1D Dark Grey Metallic'});
			colors.push({code: '1E', descr: '1E Silver Metallic'});
			colors.push({code: '2A', descr: '2A Medium Canyon Red'});
			colors.push({code: '2R', descr: '2R Jalepeno Red'});
			colors.push({code: '4E', descr: '4E Dark Sage'});
			colors.push({code: '7B', descr: '7B Shadow Blue'});
			colors.push({code: '9L', descr: '9L Oxford White'});
		break;
		default:
			colors.push({code: '1B', descr: '1B Medium Charcoal Metallic'});
			colors.push({code: '1C', descr: '1C Black'});
			colors.push({code: '1D', descr: '1D Dark Grey Metallic'});
			colors.push({code: '1E', descr: '1E Silver Metallic'});
			colors.push({code: '2A', descr: '2A Medium Canyon Red'});
			colors.push({code: '2R', descr: '2R Jalepeno Red'});
			colors.push({code: '4E', descr: '4E Dark Sage'});
			colors.push({code: '7B', descr: '7B Shadow Blue'});
			colors.push({code: '9L', descr: '9L Oxford White'});
			colors.push({code: '9W', descr: '9W Dark Charcoal Metallic'});		
	}
	return colors;
};