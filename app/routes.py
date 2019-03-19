from flask import render_template, request, make_response

from app import app
from app import chat_server
from time import sleep

chatServer = chat_server.Chat()

@app.route("/")
@app.route("/index")
def index():
    secret = request.cookies.get('secret')
    if chatServer.exists(secret):
        print("Already Logged in!")
        user = chatServer.get(secret)
    else:
        print("Not logged in!")
        user = {
            "id": "None",
            "username": "Default"
        }
    return render_template('index.html', title='Home', user=user)

@app.route("/chatmessage", methods=["POST"])
def chatMessage():
    secret = ""
    message = ""
    print("Message send!")
    for name, value in request.form.items():
        if name == "secret":
            secret = value
        if name == "message":
            message = value
            try:
                message = message.replace("&ENDOFLINE&", "")
            except Exception as e:
                pass
    if chatServer.exists(secret):
        print("Adding message")
        user = chatServer.get(secret)["username"]
        chatServer.addMessage(user + ":" + message)
    print("Invalid secret!")

@app.route("/chatupdate", methods=["POST"])
def chatUpdate():
    print("Requested log!")
    secret = ""
    for name, value in request.form.items():
        if name == "secret":
            secret = value
    if chatServer.exists(secret):
        print("Sending requested log")
        lines = ""
        for line in chatServer.getLog():
            lines += line + "&ENDOFLINE&"
        return lines
    print("Invalid secret!")
    return "NOT_LOGGED_IN"

@app.route("/login", methods=['POST'])
def login():
    username = ""
    userHash = ""
    print("User request login!")
    if request.method == 'POST':
        for name, value in request.form.items():
            if name == "username":
                username = value
            if name == "hash":
                userHash = value

    resp = make_response()
    print("Attempting login!")
    secret = chatServer.loginUser(username, userHash)
    if secret != "":
        print("Logged in!")
        resp.set_cookie('secret', secret)
    else:
        print("Wrong credentials give!")

    return resp

@app.route("/assets/<path:path>")
def send_assets(path):
    return app.send_static_file("assets/" + path)

@app.route("/css/<path:path>")
def send_css(path):
    return app.send_static_file("css/" + path)

@app.route("/js/<path:path>")
def send_js(path):
    return app.send_static_file("js/" + path)

