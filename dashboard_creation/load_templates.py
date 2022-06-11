#!/usr/bin/python3

import json
from os import path

TEMPLATES_DIR = 'grafana-templates'
DASHBOARDS_CONF = '/../dashboards.json'
ANALYTICS_CONF = '/../analytics.json'
ROW = 'row.json'
GRAPH = 'graph.json'
BAR_GAUGE = 'bar_gauge.json'
GAUGE = 'gauge.json'
HEAT_MAP = 'heat_map.json'
PIE_CHART = 'pie_chart.json'
STAT = 'stat.json'
TABLE = 'table.json'
TARGET = 'target.json'
TIME_SERIES = 'time_series.json'
MEASUREMENTS_DASHBOARD = 'measurements_dashboard.json'

def load_template(file):
    with open(path.join(TEMPLATES_DIR, file)) as f:
        return json.load(f)

def load_dashboard_visualizations():
    with open(path.dirname(__file__) + DASHBOARDS_CONF) as f:
        return json.load(f)

def load_analytics_conf():
    with open(path.dirname(__file__) + ANALYTICS_CONF) as f:
        return json.load(f)