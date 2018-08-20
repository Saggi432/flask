from flask import Flask, jsonify
import random
from flask import render_template
import os
import json
import time
import urllib2
from funny_quotes import quotes
from flask import make_response
from flask import request

from data_provider_service import DataProviderService

DATA_PROVIDER = DataProviderService(15)

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world";
@app.route("/goodbye")
def goodbye():
    return "Goodbye, world!"
@app.route("/hello/<name>")
def hello_name(name):
    return "Hello, {}".format(name)

@app.route("/funnyquote")
def get_quote():
    get_quotes = quotes()
    print(len(get_quotes))
    return jsonify(get_quotes)

def candidate():
    candidates = DATA_PROVIDER.get_candidates();
    return jsonify({"candidates" : candidates, "total" : len(candidates)})


##ROUTING
# 1st Parameter (/api/candidate) - route path
# 2nd Parameter (candidate) - endpoint
#3rd Parameter function which is executed


app.add_url_rule('/api/candidate', 'candidate', candidate)
   

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

