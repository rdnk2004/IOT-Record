import paho.mqtt.client as mqtt
def on_message(client, userdata, msg):
    print("Received:", msg.payload.decode())
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("iot/sensor_hivemq")
client.loop_forever()
