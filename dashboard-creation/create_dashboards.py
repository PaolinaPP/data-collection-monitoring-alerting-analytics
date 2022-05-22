#!/usr/bin/python3

import argparse
import json
from os import path
import load_templates
import sys
sys.path.append("..")
from restapp.libraries.measurements import MEASUREMENTS

TEMPLATES_DIR = 'grafana-templates'

def help_message():
    print("Dashboards are not created.")
    print("Supported measurements: {}".format(MEASUREMENTS))

def check_for_supported_measurements(measurements):
    for item in measurements:
        if item not in MEASUREMENTS:
            print('{} unsupported measurement.'.format(item))
            help_message()
            exit()

def get_dashboard_path():
    return path.join('..', 'provisioning', 'dashboards', 'Measurements.json')

def add_measurement_in_dashboard(measurement, final_dashboard):
    row_template = load_templates.get_row_template()
    panel_template = load_templates.get_graph_template()
    panels_len = len(final_dashboard["panels"])
    row_template["title"] = measurement
    row_template["id"] = panels_len+1
    if panels_len != 0:
        row_template["gridPos"]["y"] = (panels_len/2)*9
        panel_template["gridPos"]["y"] = ((panels_len/2)*9)+1
    panel_template["targets"][0]["expr"] = measurement + "{}"
    panel_template["title"] = measurement
    panel_template["id"] = panels_len+2
    final_dashboard["panels"].append(row_template)
    final_dashboard["panels"].append(panel_template)
    return final_dashboard

def create_dashboard(given_measurements):
    check_for_supported_measurements(given_measurements)
    final_dashboard = load_templates.get_dashboard_template()
    for measurement in given_measurements:
        final_dashboard = add_measurement_in_dashboard(measurement,
                                                       final_dashboard)
    with open(get_dashboard_path(), 'w') as f:
        json.dump(final_dashboard, f)
    print("Dashboard is successfully created.")
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--list', nargs='+', 
                        help='Required list of measurements.', 
                        required=True)
    args = parser.parse_args()
    create_dashboard(args.list)
    