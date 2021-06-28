#!/usr/bin/python3

from prometheus_client import Gauge

humidity = Gauge(
        'humidity',
        'the current humidity in percentage, this is a gauge as the value can increase or decrease'
)