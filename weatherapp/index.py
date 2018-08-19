from flask import Flask
from flask import render_template
import os
import json
import time
import urllib2

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


def get_weather():
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=london&cnt=10&mode=json&units=metric"
    response = urllib3.urlopen(url).read()
    return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

