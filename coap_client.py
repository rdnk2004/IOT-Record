import asyncio
import aiocoap
async def main():
    client = await aiocoap.Context.create_client_context()
    req = aiocoap.Message(code=aiocoap.GET, uri='coap://127.0.0.1/sensor')
    res = await client.request(req).response
    print("Received:", res.payload.decode())
    await client.shutdown()
asyncio.run(main())