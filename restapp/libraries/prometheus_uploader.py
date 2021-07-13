#!/usr/bin/python3

from prometheus_client import start_http_server, Summary, CollectorRegistry, Gauge, push_to_gateway
from .measurements import MEASUREMENTS
import random
import time

class PrometheusClient:

    def __init__(self):
        start_http_server(8000)
        self.registry = CollectorRegistry()
        self.measurements_list = {}
    
    def create_measurement_gauge(self, measurement):
        measurement_gauge = Gauge(
                    measurement,
                    'Measurement value.'
        )
        return measurement_gauge

    
    def process_request(self, data):
        for measurement in data["measurements"]:
            print(measurement)
            if measurement["measurement"] not in self.measurements_list:
                self.measurements_list[measurement["measurement"]] = self.create_measurement_gauge(measurement["measurement"])
            self.measurements_list[measurement["measurement"]].set(measurement["value"])
        return True
