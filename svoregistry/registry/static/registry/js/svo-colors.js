var svoColorChoices = function(year) {
	var colors = {};
	colors.oneB	  = {code: '1B', descr: '1B Medium Charcoal Metallic'};
	colors.oneC   = {code: '1C', descr: '1C Black'};
	colors.oneD   = {code: '1D', descr: '1D Dark Grey Metallic'};
	colors.oneE   = {code: '1E', descr: '1E Silver Metallic'};
	colors.twoA   = {code: '2A', descr: '2A Medium Canyon Red'};
	colors.twoR   = {code: '2R', descr: '2R Jalepeno Red'};
	colors.fourE  = {code: '4E', descr: '4E Dark Sage'};
	colors.sevenB = {code: '7B', descr: '7B Shadow Blue'};
	colors.nineL  = {code: '9L', descr: '9L Oxford White'};
	colors.nineW  = {code: '9W', descr: '9W Dark Charcoal Metallic'};
	switch(year) {
		case '1984':
			return	[	colors.oneC, 
						colors.oneE,
						colors.twoA,
						colors.nineW];
		break;
		case '1985':
			return	[	colors.oneB,
						colors.oneC,
						colors.oneE,
						colors.twoA,
						colors.twoR,
						colors.fourE,
						colors.nineL];
		break;
		case '1985.5':
			return	[	colors.oneB,
						colors.oneC,
						colors.oneE,
						colors.twoA,
						colors.twoR,
						colors.fourE,
						colors.nineL];	
		break;
		case '1986':
			return	[	colors.oneC,
						colors.oneD,
						colors.oneE,
						colors.twoA,
						colors.twoR,
						colors.fourE,
						colors.sevenB,
						colors.nineL];
		break;
		default:
			return	[	colors.oneB,
						colors.oneC,
						colors.oneD,
						colors.oneE,
						colors.twoA,
						colors.twoR,
						colors.fourE,
						colors.sevenB,
						colors.nineL,
						colors.nineW];
	}
};