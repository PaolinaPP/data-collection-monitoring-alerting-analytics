#!/usr/bin/python3

from flask import Flask, request, abort
from datetime import datetime
import json
import random
import time
import libraries.minio_uploader as mu
import libraries.prometheus_uploader as pu
from libraries.measurements import MEASUREMENTS

app = Flask(__name__)
prom = pu.PrometheusClient()

def check_for_correct_measurement(measurement):
    if measurement["measurement"] in MEASUREMENTS:
        return True
    else:
        return False

@app.route('/', methods=['POST'])
def post():
    data = json.loads(request.data)
    for measurement in data["measurements"]:
        if not check_for_correct_measurement(measurement):
            print("Unsupported measurement {}".format(measurement["measurement"]))
            abort(500)
    now = datetime.now()
    minio = mu.MinioClient(data, now, "logs-app-bucket")
    prom.process_request(data)
    minio.check_bucket()
    minio.write_to_minio()
    return {'success': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
