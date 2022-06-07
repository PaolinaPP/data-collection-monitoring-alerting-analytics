#!/usr/bin/python3

import json
import load_templates as load_temp

def get_panels_len_and_add_row(name, final_dashboard):
    panels_len = len(final_dashboard["panels"]) + 1
    #final_dashboard = add_row(name, final_dashboard, panels_len)
    return (final_dashboard, panels_len)

def fill_panel_width(measurements, panel_template):
    if len(measurements) <= 1:
        panel_template["gridPos"]["w"] = 6
    elif len(measurements) >= 2 and len(measurements) <= 3:
        panel_template["gridPos"]["w"] = 12
    elif len(measurements) >= 4:
        panel_template["gridPos"]["w"] = 24
    return panel_template

def set_fixed_panel_size(visualization, panel_template):
    if "size" in visualization:
        if visualization["size"] == "full":
            panel_template["gridPos"]["w"] = 24
        elif visualization["size"] == "medium":
            panel_template["gridPos"]["w"] = 12
        elif visualization["size"] == "full":
            panel_template["gridPos"]["w"] = 24
    return panel_template

def fill_panel_x_and_y(panel_template):
    return panel_template

def fill_panel_data(visualization, panel_template, final_dashboard):
    (final_dashboard, panels_len) = get_panels_len_and_add_row(visualization["name"], final_dashboard)
    print(panels_len)
    panel_template["gridPos"]["h"] = 11
    if "size" in visualization:
        panel_template = set_fixed_panel_size(visualization, panel_template)
    else:
        panel_template = fill_panel_width(visualization["measurements"], panel_template)
    if panels_len % 2 != 0:
        panel_template["gridPos"]["x"] = 0
        panel_template["gridPos"]["y"] = ((panels_len/2)*11)+1.5
    if panels_len % 2 == 0:
        panel_template["gridPos"]["x"] = 12
        panel_template["gridPos"]["y"] = ((panels_len/2)*11)+1
    panel_template = add_targets(visualization["measurements"], panel_template)
    panel_template["title"] = visualization["name"]
    panel_template["id"] = panels_len+2
    final_dashboard["panels"].append(panel_template)
    print(panel_template["gridPos"]["x"], panel_template["gridPos"]["y"], panel_template["gridPos"]["w"])
    return final_dashboard

def add_bar_gauge(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.BAR_GAUGE)
    return fill_panel_data(visualization, panel_template, final_dashboard)

def add_gauge(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.GAUGE)
    if "calcs" in visualization:
        # calcs options: "mean", "max", "min", "lastNotNull"
        panel_template["options"]["reduceOptions"]["calcs"] = visualization["calcs"]
    return fill_panel_data(visualization, panel_template, final_dashboard)

def add_graph(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.GRAPH)
    if "analytics" in visualization:
        if visualization["analytics"] == True:
            panel_template["legend"]["alignAsTable"] = json.dumps(True)
            panel_template["legend"]["avg"] = json.dumps(True)
            panel_template["legend"]["current"] = json.dumps(True)
            panel_template["legend"]["max"] = json.dumps(True)
            panel_template["legend"]["min"] = json.dumps(True)
            panel_template["legend"]["show"] = json.dumps(True)
            panel_template["legend"]["total"] = json.dumps(True)
            panel_template["legend"]["values"] = json.dumps(True)
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
        row_template["gridPos"]["y"] = (panels_len/2)*11
    final_dashboard["panels"].append(row_template)
    return final_dashboard

def add_stat(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.STAT)
    if "calcs" in visualization:
        # calcs options: "mean", "max", "min", "lastNotNull"
        panel_template["options"]["reduceOptions"]["calcs"] = visualization["calcs"]
    return fill_panel_data(visualization, panel_template, final_dashboard)

def add_table(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.TABLE)
    return fill_panel_data(visualization, panel_template, final_dashboard)

def add_targets(measurements, panel_template):
    for m in range(len(measurements)):
        target_template = load_temp.load_template(load_temp.TARGET)
        target_template["expr"] = measurements[m]["type"] + "{}"
        target_template["refId"] = measurements[m]["type"]
        target_template["legendFormat"] = measurements[m]["type"]
        panel_template["targets"].append(target_template)
    return panel_template

def add_time_series(visualization, final_dashboard):
    panel_template = load_temp.load_template(load_temp.TIME_SERIES)
    return fill_panel_data(visualization, panel_template, final_dashboard)
