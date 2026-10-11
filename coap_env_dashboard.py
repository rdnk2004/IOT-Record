import streamlit as st
import asyncio
import requests
import json
import aiocoap
db_url = "https://YOUR_PROJECT.supabase.co/rest/v1/env_data"
db_headers = {"apikey": "YOUR_KEY", "Authorization": "Bearer YOUR_KEY", "Content-Type": "application/json"}
st.title("Environmental Monitoring Dashboard")
async def fetch():
    client = await aiocoap.Context.create_client_context()
    req = aiocoap.Message(code=aiocoap.GET, uri='coap://127.0.0.1/environment')
    res = await client.request(req).response
    await client.shutdown()
    return json.loads(res.payload.decode())
if st.button("Fetch Data"):
    data = asyncio.run(fetch())
    try:
        requests.post(db_url, json=data, headers=db_headers)
    except Exception:
        pass
    col1, col2 = st.columns(2)
    col1.metric("Temperature", f"{data['temperature']} °C")
    col1.metric("Humidity", f"{data['humidity']} %")
    col2.metric("European AQI", data['aqi'])
    col2.metric("PM 2.5", f"{data['pm25']} µg/m³")
