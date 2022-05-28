#!/usr/bin/python3

import json
import load_templates as load_temp

def get_panels_len_and_add_row(name, final_dashboard):
    panels_len = len(final_dashboard["panels"])
    final_dashboard = add_row(name, final_dashboard, panels_len)
    return (final_dashboard, panels_len)

def fill_panel_data(visualization, panel_template, final_dashboard):
    (final_dashboard, panels_len) = get_panels_len_and_add_row(visualization["name"], final_dashboard)
    if panels_len != 0:
        panel_template["gridPos"]["y"] = ((panels_len/2)*9)+1
    panel_template = add_targets(visualization["measurements"], panel_template)
    panel_template["title"] = visualization["name"]
    panel_template["id"] = panels_len+2
    final_dashboard["panels"].append(panel_template)
    return final_dashboard

def add_bar_gauge(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.BAR_GAUGE)
    return fill_panel_data(visualization, panel_template, final_dashboard)

def add_gauge(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.GAUGE)
    return fill_panel_data(visualization, panel_template, final_dashboard)

def add_graph(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.GRAPH)
    return fill_panel_data(visualization, panel_template, final_dashboard)

def add_heat_map(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.HEAT_MAP)
    return fill_panel_data(visualization, panel_template, final_dashboard)

def add_pie_chart(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.PIE_CHART)
    return fill_panel_data(visualization, panel_template, final_dashboard)

def add_row(name, final_dashboard, panels_len):
    row_template = load_temp.load_template(load_temp.ROW)
    row_template["title"] = name
    row_template["id"] = panels_len + 1
    if panels_len != 0:
        row_template["gridPos"]["y"] = (panels_len/2)*9
    final_dashboard["panels"].append(row_template)
    return final_dashboard

def add_stat(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.STAT)
    return fill_panel_data(visualization, panel_template, final_dashboard)

def add_table(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.TABLE)
    return fill_panel_data(visualization, panel_template, final_dashboard)

def add_targets(measurements, panel_template):
    for m in range(len(measurements)):
        target_template = load_temp.load_template(load_temp.TARGET)
        target_template["expr"] = measurements[m]["type"] + "{}"
        target_template["refId"] = measurements[m]["type"]
        panel_template["targets"].append(target_template)
    return panel_template

def add_time_series(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.TIME_SERIES)
    return fill_panel_data(visualization, panel_template, final_dashboard)
