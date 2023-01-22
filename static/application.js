var socket;
var interval = 1;
var timeOutId;
window.addEventListener("load", function(){
    console.log("window ready!!");
    //connect to the socket server.
    //socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];
    socket.on('my response', function(recieved) {
	    console.log(recieved.data);
	    document.getElementById("currentTime").innerHTML = recieved.data;
	    timeOutId = setTimeout(()=>socket.emit('updateTime', {data: 'recieved latest!'}), interval);
	    
	    document.querySelector("#seconds").addEventListener("change", (e)=>{
	    	interval = e.target.value;
	    	clearTimeout(timeOutId);
	    	timeOutId = setTimeout(()=>socket.emit('updateTime', {data: 'recieved latest!'}), interval);
	    });
    });
    
    
    

});
