import streamlit as st
import asyncio
import json
import time
import aiocoap
st.title("CoAP Sensor Dashboard")
t_col = st.empty()
h_col = st.empty()
async def fetch():
    client = await aiocoap.Context.create_client_context()
    req = aiocoap.Message(code=aiocoap.GET, uri='coap://127.0.0.1/sensor')
    res = await client.request(req).response
    await client.shutdown()
    return json.loads(res.payload.decode())
while True:
    data = asyncio.run(fetch())
    t_col.metric("Temperature", f"{data['temperature']} °C")
    h_col.metric("Humidity", f"{data['humidity']} %")
    time.sleep(2)
