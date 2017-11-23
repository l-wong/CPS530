function loadContent() {
	var xmlhttp;
	
	if (window.XMLHttpRequest) {
		xmlhttp = new XMLHttpRequest();
	}
	else {
		xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.open("GET","lab07.xml",false);
	xmlhttp.send();
	xmlDocument=xmlhttp.responseXML;
		console.log(xmlDocument);
	
    document.getElementById("RADIONAME").innerHTML = xmlDocument.getElementsByTagName("radioname")[0].childNodes[0].nodeValue;
    var radiourl = xmlDocument.getElementsByTagName("radurl")[0].childNodes[0].nodeValue;
    document.getElementById("RADURL").href = radiourl;
    document.getElementById("RADURL").innerHTML = radiourl;
    document.getElementById("ARTIST").innerHTML = xmlDocument.getElementsByTagName("artists")[0].childNodes[0].nodeValue;
    document.getElementById("TITLE").innerHTML = xmlDocument.getElementsByTagName("title")[0].childNodes[0].nodeValue;
    document.getElementById("COVER").src = xmlDocument.getElementsByTagName("cover")[0].childNodes[0].nodeValue;
	var dur = xmlDocument.getElementsByTagName("playduration")[0].childNodes[0].nodeValue;
	dur = parseInt(dur, 10);
	dur = secondsToTime(dur);
	document.getElementById("DURATION").innerHTML = dur;


}

function secondsToTime(useconds) {
	var hrs = Math.floor(useconds / (100 * 60 * 60));
	var hrs_rem = useconds / (100 * 60 * 60) - hrs;
	var min = Math.floor(hrs_rem * 60);
	var min_rem = hrs_rem * 60 - min;
	var sec = Math.floor(min_rem * 60);
	var sec_rem = min_rem * 60 - sec;
	var usec = Math.floor(sec_rem * 100);
	return hrs + ":" + min + ":" + sec + ":" + usec;
}
