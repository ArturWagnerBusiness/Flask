

function login() {
	var username = document.getElementById("chat_input_username").value;
	var password = document.getElementById("chat_input_password").value;
	var hash = SHA256(password);
	console.log(hash);



	var xhr = new XMLHttpRequest();
    xhr.open("POST", "/login", true);
	xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
	
	xhr.send("username=" +  username + "&hash=" + hash);
}

function sendMessage(){
	var xhr = new XMLHttpRequest();
    xhr.open("POST", "/chatmessage", true);
	xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
	
	xhr.send("secret=" +  getCookie("secret") + "&message=" + document.getElementById('message_input').value)
}

function update(){
	var xhr = new XMLHttpRequest();
    xhr.open("POST", "/chatupdate", true);
	xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
	xhr.onload = function(event){ 
		if (event.target.response !== "NOT_LOGGED_IN") {
			document.getElementsByClassName("display")[0].innerHTML = "";
			var thing = event.target.response.split("&ENDOFLINE&");
			for (var i = 0; i < thing.length; i++) {
				username = thing[i].split(":")[0];
				message = thing[i].replace(username + ":", "");
				var formatedmessage = formatMessage(username, message);
				document.getElementsByClassName("display")[0].innerHTML += formatedmessage;
			};
		}
	}; 
	xhr.send("secret=" +  getCookie("secret"));
}
function formatMessage(username, message){
	obj = '<div class="message"><div class="user">'+username+':</div><div class="text">'+message+'</div></div>';
	return obj;
}
function getCookie(cname) {
	var name = cname + "=";
	var decodedCookie = decodeURIComponent(document.cookie);
	var ca = decodedCookie.split(';');
	for(var i = 0; i <ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0) == ' ') {
			c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {
			return c.substring(name.length, c.length);
		}
	}
	return "";
}

//var connection = new Connection("82.42.187.52", 14901)

//database.validateUser("artur112", "c3c354bdcd85aca584a2a56227407dc9deb8ae3c9623e798023db3b32989d19b")
