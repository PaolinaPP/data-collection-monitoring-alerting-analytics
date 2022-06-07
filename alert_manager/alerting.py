#!/usr/bin/python3

from flask import Flask, request, abort
from datetime import datetime
from os import path
import json
import random
import time
import notifier

ALERTS_CONF = 'alerts.json'
ALERTS_DATA = None
ALERTS_REPEATED = {}
app = Flask(__name__)


def load_dashboard_visualizations():
    with open(path.dirname(__file__) + ALERTS_CONF) as f:
        return json.load(f)


def create_dict_repeated_measurements():
    global ALERTS_REPEATED
    for measurement_alert in ALERTS_DATA["alert_rules"]:
        ALERTS_REPEATED[measurement_alert["type"]] = 0


@app.route('/', methods=['POST'])
def post():
    global ALERTS_REPEATED
    data = json.loads(request.data)
    for measurement in data["measurements"]:
        for measurement_alert in ALERTS_DATA["alert_rules"]:
            if measurement["measurement"] == measurement_alert["type"]:
                if measurement["value"] > measurement_alert["max"] or measurement["value"] < measurement_alert["min"]:
                    ALERTS_REPEATED[measurement_alert["type"]] += 1
                    if ALERTS_REPEATED[measurement_alert["type"]] > measurement_alert["repeat"]:
                        if ALERTS_DATA["notifier"] == "slack":
                            notifier.send_slack_notification(ALERTS_DATA["webhookurl"], \
                                                            measurement)
                else:
                    ALERTS_REPEATED[measurement_alert["type"]] = 0
    return {'success': 'success'}


if __name__ == '__main__':
    ALERTS_DATA = load_dashboard_visualizations()
    create_dict_repeated_measurements()
    app.run(host='0.0.0.0', port=2020, threaded=True)