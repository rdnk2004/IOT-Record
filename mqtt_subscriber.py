import paho.mqtt.client as mqtt
import requests
import json
url = "https://YOUR_PROJECT.supabase.co/rest/v1/sensor_data"
headers = {"apikey": "YOUR_KEY", "Authorization": "Bearer YOUR_KEY", "Content-Type": "application/json"}
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    requests.post(url, json=data, headers=headers)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("iot/sensor_data")
client.loop_forever()
