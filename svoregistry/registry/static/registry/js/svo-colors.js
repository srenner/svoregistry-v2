var svoColorChoices = function(year) {
	var colors = [];
	var allColors = {};
	allColors.oneB	 = {code: '1B', descr: '1B Medium Charcoal Metallic'};
	allColors.oneC   = {code: '1C', descr: '1C Black'};
	allColors.oneD   = {code: '1D', descr: '1D Dark Grey Metallic'};
	allColors.oneE   = {code: '1E', descr: '1E Silver Metallic'};
	allColors.twoA   = {code: '2A', descr: '2A Medium Canyon Red'};
	allColors.twoR   = {code: '2R', descr: '2R Jalepeno Red'};
	allColors.fourE  = {code: '4E', descr: '4E Dark Sage'};
	allColors.sevenB = {code: '7B', descr: '7B Shadow Blue'};
	allColors.nineL  = {code: '9L', descr: '9L Oxford White'};
	allColors.nineW  = {code: '9W', descr: '9W Dark Charcoal Metallic'};
	switch(year) {
		case '1984':
			colors.push(allColors.oneC);
			colors.push(allColors.oneE);
			colors.push(allColors.twoA);
			colors.push(allColors.nineW);
		break;
		case '1985':
			colors.push(allColors.oneB);
			colors.push(allColors.oneC);
			colors.push(allColors.oneE);
			colors.push(allColors.twoA);
			colors.push(allColors.twoR);
			colors.push(allColors.fourE);
			colors.push(allColors.nineL);
		break;
		case '1985.5':
			colors.push(allColors.oneB);
			colors.push(allColors.oneC);
			colors.push(allColors.oneE);
			colors.push(allColors.twoA);
			colors.push(allColors.twoR);
			colors.push(allColors.fourE);
			colors.push(allColors.nineL);		
		break;
		case '1986':
			colors.push(allColors.oneC);
			colors.push(allColors.oneD);
			colors.push(allColors.oneE);
			colors.push(allColors.twoA);
			colors.push(allColors.twoR);
			colors.push(allColors.fourE);
			colors.push(allColors.sevenB);
			colors.push(allColors.nineL);
		break;
		default:
			colors.push(allColors.oneB);
			colors.push(allColors.oneC);
			colors.push(allColors.oneD);
			colors.push(allColors.oneE);
			colors.push(allColors.twoA);
			colors.push(allColors.twoR);
			colors.push(allColors.fourE);
			colors.push(allColors.sevenB);
			colors.push(allColors.nineL);
			colors.push(allColors.nineW);		
	}
	return colors;
};