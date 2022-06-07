#!/usr/bin/python3

import json
import load_templates as load_temp

ANALYTICS_DASHBOARD = {
        "name": "Analytics",
        "visualizations": [
            {
                "type": "graph",
                "name": "Measurements",
                "measurements": [],
                "analytics": True,
                "size": "full"
            }
        ]
    }

def fill_analytics_measurements():
    global ANALYTICS_DASHBOARD
    analytics_config = load_temp.load_analytics_conf()
    for visual in ANALYTICS_DASHBOARD["visualizations"]:
        for measurement in range(len(analytics_config["measurements"])):
            visual["measurements"].append(analytics_config["measurements"][measurement])
    return ANALYTICS_DASHBOARD


