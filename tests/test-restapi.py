import requests
import json
import time
import random

payload = {
  "measurements":
    [
        { 
            "measurement": "temperature",
            "value" : "23.0"
        },
        {
            "measurement": "humidity",
            "value" : "23.0"
        },
        {
            "measurement": "cpu",
            "value" : "23.0"
        },
        {
            "measurement": "storage",
            "value" : "23.0"
        }
    ]
}
while(1):
    for i in range(4):
        payload["measurements"][i]["value"] = random.randint(20, 30)
    print(payload)
    response = requests.post('http://127.0.0.1:5000', data = json.dumps(payload))
    print(response)
    time.sleep(15)
    