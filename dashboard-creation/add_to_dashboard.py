#!/usr/bin/python3

import json
import load_templates as load_temp

def add_bar_gauge(measurement, final_dashboard):
    return final_dashboard

def add_gauge(measurement, final_dashboard):
    return final_dashboard

def add_graph(measurement, final_dashboard):
    panels_len = len(final_dashboard["panels"])
    final_dashboard = add_row(measurement, final_dashboard, panels_len)
    panel_template = load_temp.load_template(load_temp.GRAPH)
    if panels_len != 0:
        panel_template["gridPos"]["y"] = ((panels_len/2)*9)+1
    panel_template["targets"][0]["expr"] = measurement + "{}"
    panel_template["title"] = measurement
    panel_template["id"] = panels_len+2
    final_dashboard["panels"].append(panel_template)
    return final_dashboard

def add_heat_map(measurement, final_dashboard):
    return final_dashboard

def add_pie_chart(measurement, final_dashboard):
    return final_dashboard

def add_row(measurement, final_dashboard, panels_len):
    row_template = load_temp.load_template(load_temp.ROW)
    row_template["title"] = measurement
    row_template["id"] = panels_len + 1
    if panels_len != 0:
        row_template["gridPos"]["y"] = (panels_len/2)*9
    final_dashboard["panels"].append(row_template)
    return final_dashboard

def add_stat(measurement, final_dashboard):
    return final_dashboard

def add_table(measurement, final_dashboard):
    return final_dashboard

def add_target(measurement, final_dashboard):
    return final_dashboard

def add_time_series(measurement, final_dashboard):
    return final_dashboard
