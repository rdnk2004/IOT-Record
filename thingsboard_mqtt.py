import paho.mqtt.client as mqtt
import json
import random
import time
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set("YOUR_ACCESS_TOKEN")
client.connect("thingsboard.cloud", 1883, 60)
while True:
    payload = {"temperature": round(random.uniform(20.0, 35.0), 2), "humidity": round(random.uniform(40.0, 80.0), 2)}
    client.publish("v1/devices/me/telemetry", json.dumps(payload))
    time.sleep(5)