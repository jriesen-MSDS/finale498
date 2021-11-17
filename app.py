#copied and updated from Prof Gift
from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import requests

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    html = f"<h3>For MSDS 498</h3>"
    return html.format(format)

@app.route('/hi/<name>')
def hello(name):
    greeting = f"Hello: {name}"
    return jsonify(greeting)

@app.route('/Info/<response>')
def resp(response):
    url = "https://6l6l7n7vtb.execute-api.us-east-2.amazonaws.com/test/predict"

    payload="{\"data\":\"0,-0.34147611300851444,0.18202662446267728,310000.0,2.0,2.0,1.0,44.0,-1.0,-1.0,-2.0,-2.0,-2.0,-2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\"}"
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
