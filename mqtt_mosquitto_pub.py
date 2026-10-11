import paho.mqtt.client as mqtt
import json
import random
import time
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
try:
    client.connect("localhost", 1883, 1)
except Exception:
    pass
while True:
    data = {"temperature": round(random.uniform(20.0, 35.0), 2), "humidity": round(random.uniform(40.0, 80.0), 2)}
    try:
        client.publish("iot/sensor_mosquitto", json.dumps(data))
    except Exception:
        pass
    print("Published to Mosquitto (localhost:1883):", json.dumps(data), flush=True)
    time.sleep(5)
