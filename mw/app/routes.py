from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)      
 
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/template')
def staticPage():
    return render_template("hello.html")

@app.route('/welcome')
def welcomePage():
    return render_template("welcome.html")

@app.route('/height')
def heightPage():
    height = queryHeight()
    app.logger.info("height: " + str(height))
    return render_template("height.html", height=height)

@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    error = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        app.logger.info("username: " + username + " password: " + password)
        if (username == "admin") or (password == "admin"):
            return redirect(url_for("home"))
        else:
            error = "invalid credentials"
    return render_template("login.html", error=error)

@app.route('/write', methods=['POST'])
def write():
    res = request.get_json(force=True)
    print(res)
    return "success"

@app.route('/createNode', methods=['POST'])
def createNode():
    jsonReq = request.get_json(force=True)
    app.logger.info(jsonReq)

    node = jsonReq["node"]
    x = node["x"]
    app.logger.info(x)

    return "success!!"

@app.route('/receive')
def receive():
    message = {
        'page': "receive",
        'message': "receive get"
    }
    jsonMessage = json.dumps(message)
    return jsonMessage

def queryHeight():
    height = 3
    return height

if __name__ == '__main__':
  app.run(debug=True)
