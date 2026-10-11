import streamlit as st
import requests
import time
url = "https://YOUR_PROJECT.supabase.co/rest/v1/sensor_data?select=*&order=id.desc&limit=1"
headers = {"apikey": "YOUR_KEY", "Authorization": "Bearer YOUR_KEY"}
st.title("MQTT Sensor Dashboard")
t_col = st.empty()
h_col = st.empty()
while True:
    data = requests.get(url, headers=headers).json()
    if data:
        t_col.metric("Temperature", f"{data[0]['temperature']} °C")
        h_col.metric("Humidity", f"{data[0]['humidity']} %")
    time.sleep(2)
