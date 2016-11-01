var fileInput;
var reader = new FileReader();

window.onload = function(){
	fileInput = document.getElementById("fileSelector")
	fileInput.addEventListener("change", loadFile, false);
}


function loadFile(e){
	var file = e.target.files;
	
	reader.readAsText(file[0]);
	
	reader.onload = function(e){
		parseFile(reader.result);
	}
}

function parseFile(d){
	var data = d.split("end#");
	data.pop();
	var block;
	
	console.log("Number of data blocks: " + data.length);
	
	for(var i = 0; i < data.length; i++){
		block = data[i].split(/[\n|]/);
		block.pop();
		console.log("Block " + (i+1) + ":");
		console.log("   Block type: " + block[0].replace(/#/g, ""));
		
		for(var j = 1; j < block.length; j++){
			console.log("   Identifier: " + block[j].split(":")[0] + "   Value: " + block[j].split(":")[1]);
		}
		
		parseMapl(data[i].split(/[\n|:]/));
	}
}

function parseMapl(b){
	var mapl = b[b.indexOf("mapl")+1].split(".");
	var period = parseInt(b[b.indexOf("size")+1]);
	var sx, sy, ox, oy, pt;
	
	console.log("Pattern:");
	
	//handle invalid input
	
	if(mapl.length != period * 5){
		console.error("Mapl parse error: Invalid size or mapl length!");
		console.info("Adjusting period to match mapl.");
		period = Math.floor(mapl.length/5);
	}
	

	for(var i = 0; i < period; i ++){
		sx = parseInt(mapl[i*5]);
		ox = parseInt(mapl[i*5 + 1]);
		sy = parseInt(mapl[i*5 + 2]);
		oy = parseInt(mapl[i*5 + 3]);
		pt = parseInt(mapl[i*5 + 4], 16).toString(2).replace(/0/g, '_').replace(/1/g, '#');
		while(pt.length < sx*sy) pt = "_" + pt;
		
		console.log(i+1 + ".");
		
		for(var j = 0; j < sy; j++){
			console.log(pt.slice(j*sx, (j+1)*sx));
		}
	}
}