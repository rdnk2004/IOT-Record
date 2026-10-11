import asyncio
import json
import random
import aiocoap.resource as resource
import aiocoap
class SensorResource(resource.Resource):
    async def render_get(self, request):
        data = {"temperature": round(random.uniform(20.0, 35.0), 2), "humidity": round(random.uniform(40.0, 80.0), 2)}
        return aiocoap.Message(payload=json.dumps(data).encode())
async def main():
    root = resource.Site()
    root.add_resource(['sensor'], SensorResource())
    await aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683))
    await asyncio.get_running_loop().create_future()
asyncio.run(main())
