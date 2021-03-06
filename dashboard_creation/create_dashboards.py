#!/usr/bin/python3

import json
from os import path
import load_templates as load_temp
import add_to_dashboard as dashboard
import analytics_dashboard as analytics

def get_dashboard_path(dashboard):
    return path.join('..', 'provisioning', 'dashboards', dashboard+".json")

def create_dashboard():
    dashboard_config = load_temp.load_dashboard_visualizations()
    dashboard_config.append(analytics.fill_analytics_measurements())
    for dash in range(len(dashboard_config)):
        final_dashboard = load_temp.load_template(load_temp.MEASUREMENTS_DASHBOARD)
        final_dashboard["title"] = dashboard_config[dash]["name"]
        final_dashboard["id"] = dash + 1
        for visual in dashboard_config[dash]["visualizations"]:
            print("visual ", visual)
            if visual["type"] == "bar_gauge":
                final_dashboard = dashboard.add_bar_gauge(visual, final_dashboard)
            elif visual["type"] == "gauge":
                final_dashboard = dashboard.add_gauge(visual, final_dashboard)
            elif visual["type"] == "graph":
                final_dashboard = dashboard.add_graph(visual, final_dashboard)
            elif visual["type"] == "heat_map":
                final_dashboard = dashboard.add_heat_map(visual, final_dashboard)
            elif visual["type"] == "pie_chart":
                final_dashboard = dashboard.add_pie_chart(visual, final_dashboard)
            elif visual["type"] == "stat":
                final_dashboard = dashboard.add_stat(visual, final_dashboard)
            elif visual["type"] == "table":
                final_dashboard = dashboard.add_table(visual, final_dashboard)
            elif visual["type"] == "time_series":
                final_dashboard = dashboard.add_time_series(visual, final_dashboard)
        with open(get_dashboard_path(dashboard_config[dash]["name"]), 'w') as f:
            json.dump(final_dashboard, f)
        print("Dashboard is successfully created.")

    return True

if __name__ == '__main__':
    create_dashboard()