from flask import Flask, render_template, request
import json

app = Flask(__name__)      
 
@app.route('/')
def home():
    return "hi"

@app.route('/template')
def staticPage():
    return render_template("hello.html")

@app.route('/welcome')
def welcomePage():
    return render_template("welcome.html")

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

if __name__ == '__main__':
  app.run(debug=True)
