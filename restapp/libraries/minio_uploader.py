#!/usr/bin/python3

from minio import Minio
from minio.error import S3Error
from datetime import datetime
from .measurements import MEASUREMENTS
import json
import os

class MinioClient():

    def __init__(self, data, datetime_now, bucket):
        self.data = data
        self.datetime_now = datetime_now
        self.bucket = bucket
        self.client = Minio(
            "127.0.0.1:9000",
            access_key="minio",
            secret_key="minio123",
            secure = False
        )

    def generate_minio_filename(self, measurement):
        return str(self.datetime_now.strftime("%d-%m-%Y")) + '/' + \
               str(self.datetime_now.strftime("%H:%M:%S")) + '/' + \
               str(measurement["measurement"]) + ".json"

    def write_to_minio(self):
        for measurement in self.data["measurements"]:
            file_contant = measurement["value"]
            with open('data.json', 'w') as f:
                json.dump(file_contant, f)
            local_path = os.getcwd() + '/data.json'
            minio_filename = self.generate_minio_filename(measurement)
            self.client.fput_object(self.bucket, minio_filename, local_path)  

    def check_bucket(self):
        found = self.client.bucket_exists("logs-app-bucket")
        if not found:
            client.make_bucket("logs-app-bucket")
        else:
            print("Bucket 'logs-app-bucket' already exists")

    