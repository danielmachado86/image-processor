import asyncio
import os
from dotenv import load_dotenv
import websockets

from azure.messaging.webpubsubservice import WebPubSubServiceClient

load_dotenv()


async def connect(url):
    async with websockets.connect(url) as ws:
        print("connected")
        while True:
            print("Received message: " + await ws.recv())


if __name__ == "__main__":

    service = WebPubSubServiceClient.from_connection_string(
        os.getenv("CONNECTION_STRING"), hub="Hub1"
    )
    token = service.get_client_access_token()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        asyncio.run(connect(token["url"]))
    except KeyboardInterrupt:
        pass
