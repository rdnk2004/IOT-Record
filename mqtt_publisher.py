import paho.mqtt.client as mqtt
import json
import random
import time
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("broker.hivemq.com", 1883, 60)
while True:
    payload = {"temperature": round(random.uniform(20.0, 35.0), 2), "humidity": round(random.uniform(40.0, 80.0), 2)}
    client.publish("iot/sensor_data", json.dumps(payload))
    time.sleep(5)
