import asyncio
import json
import requests
import aiocoap.resource as resource
import aiocoap
w_url = "https://api.open-meteo.com/v1/forecast?latitude=10.0159&longitude=76.3419&current=temperature_2m,relative_humidity_2m,weather_code"
a_url = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=10.0159&longitude=76.3419&current=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,ozone,european_aqi"
class EnvResource(resource.Resource):
    async def render_get(self, request):
        w = requests.get(w_url).json()['current']
        a = requests.get(a_url).json()['current']
        data = {"temperature": w['temperature_2m'], "humidity": w['relative_humidity_2m'], "aqi": a['european_aqi'], "pm25": a['pm2_5']}
        return aiocoap.Message(payload=json.dumps(data).encode())
async def main():
    root = resource.Site()
    root.add_resource(['environment'], EnvResource())
    await aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683))
    await asyncio.get_running_loop().create_future()
asyncio.run(main())