#!/usr/bin/python3

from flask import Flask, request, abort
from datetime import datetime
import requests
import json
import random
import time
import libraries.minio_uploader as mu
import libraries.prometheus_uploader as pu
from libraries.measurements import MEASUREMENTS

app = Flask(__name__)
prom = pu.PrometheusClient()
minio = mu.MinioClient("logs-app-bucket")
to_sleep = True

def check_for_correct_measurement(measurement):
    if measurement["measurement"] in MEASUREMENTS:
        return True
    else:
        return False

@app.route('/', methods=['POST'])
def post():
    global to_sleep
    data = json.loads(request.data)
    response = requests.post('http://127.0.0.1:2020', data = json.dumps(data))
    # if response != 200:
    #     abort(500)
    for measurement in data["measurements"]:
        if not check_for_correct_measurement(measurement):
            print("Unsupported measurement {}".format(measurement["measurement"]))
            abort(500)
    if not prom.process_request(data):
        print("Prometheus problem.")
        abort(500)
    minio.check_bucket()
    if to_sleep:
        time.sleep(15)
        to_sleep = False
    now = datetime.now()
    if not minio.write_to_minio(data, now):
        print("Minio problem.")
        abort(500)
    return {'success': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
