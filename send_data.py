import requests
import random
import time
url = "https://YOUR_PROJECT.supabase.co/rest/v1/sensor_data"
headers = {"apikey": "YOUR_KEY", "Authorization": "Bearer YOUR_KEY", "Content-Type": "application/json"}
while True:
    data = {"temperature": round(random.uniform(20.0, 35.0), 2), "humidity": round(random.uniform(40.0, 80.0), 2)}
    requests.post(url, json=data, headers=headers)
    time.sleep(5)
