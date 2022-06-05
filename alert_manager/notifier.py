#!/usr/bin/python3

import smtplib, ssl
import json
import sys
import random
import requests

PORT = 465  # For SSL
CONTEXT = ssl.create_default_context()

def send_slack_notification(url, measurement):
    message = f" There is an alert of measurement {measurement}. \
                 Please check Grafana dashboards."
    title = (f"New Incoming Message :zap:")
    slack_data = {
        "username": "NotificationBot",
        "icon_emoji": ":satellite:",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
