import requests
import json
import time

payload = {
  "measurements":
    [
        { 
            "measurement": "temperature",
            "value" : "23.0"
        },
        {
            "measurement": "humidity",
            "value" : "27.0"
        }
    ]
}
while(1):
    response = requests.post('http://127.0.0.1:5000', data = json.dumps(payload))
    print(response)
    time.sleep(15)
    