from flask import render_template, request, make_response

from app import app
from app import chat_server

chatServer = chat_server.Chat()

@app.route("/")
@app.route("/index")
def index():
    secret = request.cookies.get('secret')
    if chatServer.exist(secret):
        user = chatServer.get(secret)

    else:
        user = {
            "id": "None",
            "username": "Default"
        }
    return render_template('index.html', title='Home', user=user)

@app.route("/chat", methods=["GET", "POST"])
def chatMessage():
    secret = ""
    message = ""
    if request.method == 'POST':
        print(request.form)
        for name, value in request.form.items():
            if name == "secret":
                secret = value
            if name == "message":
                message = value
    if chatServer.exist(secret):
        chatServer.addMessage(message)

@app.route("/login", methods=['GET', 'POST'])
def login():
    username = ""
    userHash = ""
    if request.method == 'POST':
        print(request.form)
        for name, value in request.form.items():
            if name == "username":
                username = value
            if name == "hash":
                userHash = value

    resp = make_response()
    secret = chatServer.loginUser(username, userHash)
    if secret != "":
        resp.set_cookie('secret', secret)

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

