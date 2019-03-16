

function login() {
    var username = document.getElementById("chat_input_username").value;
    var password = document.getElementById("chat_input_password").value;
    console.log(password);
    var hash = SHA256(password);


	var xhr = new XMLHttpRequest();
    xhr.open("POST", "/login", true);
	xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
	
	xhr.send("username=" +  username + "&hash=" + hash);
}

function send(){}
	var xhr = new XMLHttpRequest();
    xhr.open("POST", "/chat", true);
	xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
	
	xhr.send("secret=" +  username + "&message=" + hash);

function update(){}



//var connection = new Connection("82.42.187.52", 14901)

//database.validateUser("artur112", "c3c354bdcd85aca584a2a56227407dc9deb8ae3c9623e798023db3b32989d19b")
