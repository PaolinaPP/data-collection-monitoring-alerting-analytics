# data-collection-monitoring-alerting-analytics

## Description
This project provides a system which Collects, Stores and Monitors IOT Data.

## System components
Every component of the system is living in a separate docker container. Docker Compose is used to launch the containers, making it easier for the user, as they will not have to launch each container separately. All containers will be launched with a single command using Docker Compose. The description of each of the containers can be found in the file [docker-compose.yml](https://github.com/PaolinaPP/iot-data-collection-and-monitoring/blob/master/docker-compose.yml).

### RESTful API
RESTful API is Python application which collects data from the users and sends it to MinIO and Prometheus. The implementation of the application is in [./restapp](https://github.com/PaolinaPP/iot-data-collection-and-monitoring/tree/master/restapp) folder. The application receives data in a specific json format:
<pre>
{ 
 "measurements": 
   [
       {
           "measurement": "...",
           "value" : "..."
       },
       {
           "measurement": "...",
           "value" : "..."
       }
   ]
</pre>

### MinIO
MinIO stores data on the local device. The data is located in **./data** folder in the project directory. All the data is stored in **./data/logs-app-bucket**. The data for each day is stored in different directories (the name of the directory is the day), thus data for different days can be analyzed. The directory for the day has subdirectories whose names are the time at which the system received the measurement data. The time directories contain the files with measurement data, and the file names represent the type of measurement (eg temperature, humidity, etc.).
<pre>
logs-app-bucket/
└── 30-06-2021
    ├── 14:12:29
    │   ├── humidity.json
    │   └── temperature.json
    └── 14:13:41
        ├── humidity.json	 
        └── temperature.json
</pre>
The access to the MinIO user interface is done through a browser - the address where it is located is **http://localhost:9000/**.

### Prometheus
Promethes collects data from Python RESTful API and provides this data to Grafana. Using the configuration file [./prom/prometheus.yml](https://github.com/PaolinaPP/iot-data-collection-and-monitoring/blob/master/prom/prometheus.yml) we tell Prometheus where to read the data. The address where the data is uploaded is **http://localhost:8000/**.

### Grafana
Grafana is used to monitors IOT data. The [./provisioning](https://github.com/PaolinaPP/iot-data-collection-and-monitoring/tree/master/provisioning) directory contains pre-created dashboards, as well as configuration files that tell Grafana where to look for the data provided by Prometheus. The distribution in the [./provisioning](https://github.com/PaolinaPP/iot-data-collection-and-monitoring/tree/master/provisioning) directory is the same as it should be in the **/etc/grafana/provisioning** directory in the container:
<pre>
provisioning/ 
├── dashboards 
│   ├── dashboards.yml 
│   └── Measurements.json 
└── datasources 
    └── prom.yml 
</pre>

### Requirements
- Python3
- Docker
- Docker Compose
- Python libraries - argparse, json, os, flask, minio, minio.error, prometheus_client

### Create Dashboards
Before starting the system, you need to create your own custom dashboard to be used by Grafana. To do this, in the main directory of the project must run the Python script [create_dashboards.py](https://github.com/PaolinaPP/iot-data-collection-and-monitoring/blob/master/create_dashboards.py), which in turn as a parameter requires a sheet of measurements (eg temperature, humidity, etc.). The measurements that the system supports are described in the MEASUREMENTS list in the [./restapp/libraries/measurements.py](https://github.com/PaolinaPP/iot-data-collection-and-monitoring/blob/master/restapp/libraries/measurements.py) file. If the list does not contain a dimension that the user wants to display, he can manually add it to the list before calling the [create_dashboards.py](https://github.com/PaolinaPP/iot-data-collection-and-monitoring/blob/master/create_dashboards.py) script.
The dashboard can be created using the command **create_dashboards.py --list <list-of-measurements-separated-by-space>**
For example:
```
create_dashboards.py --list temperature humidity
```

### Run System
```
$ docker-compose up -d
```
OR
```
docker-compose up
```
To check the system is successfully started need to run the next command and verify that the 4 containers with the  components described above are up:
```
docker ps
```
Once the system is up and running, it is ready to collect and visualize user data. For this purpose, user must provide data in a predefined format at http://127.0.0.1:5000. 
[Here](https://github.com/PaolinaPP/iot-data-collection-and-monitoring/blob/master/tests/test-restapi.py) you can find an example how to send data to the system.
