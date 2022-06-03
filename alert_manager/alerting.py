#!/usr/bin/python3

from flask import Flask, request, abort
from datetime import datetime
from os import path
import json
import random
import time

DASHBOARDS_CONF = 'alerts.json'
DASHBOARDS_DATA = None
app = Flask(__name__)

def load_dashboard_visualizations():
    with open(path.dirname(__file__) + DASHBOARDS_CONF) as f:
        return json.load(f)

@app.route('/', methods=['POST'])
def post():
    data = json.loads(request.data)
    for measurement in data["measurements"]:
        for measurement in DASHBOARDS_DATA:
            print(measurement)



if __name__ == '__main__':
    DASHBOARDS_DATA = load_dashboard_visualizations()
    app.run(host='0.0.0.0', port=5000, threaded=True)