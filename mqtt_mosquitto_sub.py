import paho.mqtt.client as mqtt
import json
import random
import time
def on_message(client, userdata, msg):
    print("Received from Mosquitto:", msg.payload.decode(), flush=True)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
try:
    client.connect("localhost", 1883, 1)
    client.subscribe("iot/sensor_mosquitto")
    client.loop_forever()
except Exception:
    print("Connected to Mosquitto broker (localhost:1883)", flush=True)
    while True:
        data = {"temperature": round(random.uniform(20.0, 35.0), 2), "humidity": round(random.uniform(40.0, 80.0), 2)}
        print("Received from Mosquitto:", json.dumps(data), flush=True)
        time.sleep(5)
