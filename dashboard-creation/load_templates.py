#!/usr/bin/python3

import argparse
import json
from os import path

TEMPLATES_DIR = 'grafana-templates'

def get_row_template():
    with open(path.join(TEMPLATES_DIR, 'row.json')) as f:
        return json.load(f)

def get_graph_template():
    with open(path.join(TEMPLATES_DIR, 'graph.json')) as f:
        return json.load(f)

def get_bar_gauge_template():
    with open(path.join(TEMPLATES_DIR, 'bar_gauge.json')) as f:
        return json.load(f)

def get_gauge_template():
    with open(path.join(TEMPLATES_DIR, 'gauge.json')) as f:
        return json.load(f)

def get_heat_map_template():
    with open(path.join(TEMPLATES_DIR, 'heat_map.json')) as f:
        return json.load(f)

def get_pie_chart_template():
    with open(path.join(TEMPLATES_DIR, 'pie_chart.json')) as f:
        return json.load(f)

def get_stat_template():
    with open(path.join(TEMPLATES_DIR, 'stat.json')) as f:
        return json.load(f)

def get_table_template():
    with open(path.join(TEMPLATES_DIR, 'table.json')) as f:
        return json.load(f)

def get_target_template():
    with open(path.join(TEMPLATES_DIR, 'target.json')) as f:
        return json.load(f)

def get_time_series_template():
    with open(path.join(TEMPLATES_DIR, 'time_series.json')) as f:
        return json.load(f)

def get_dashboard_template():
    with open(path.join(TEMPLATES_DIR, 'measurements_dashboard.json')) as f:
        return json.load(f)