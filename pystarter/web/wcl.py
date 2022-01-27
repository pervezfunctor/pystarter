import asyncio
from websockets import client


async def counter():
    for cnt in range(10):
        await asyncio.sleep(1)
        yield cnt


async def consume(websocket: client.WebSocketClientProtocol) -> None:
    async for msg in websocket:
        print(str(msg))


async def produce(websocket: client.WebSocketClientProtocol):
    async for cnt in counter():
        await websocket.send(str(cnt))
    await websocket.close()


async def main():
    uri = "ws://localhost:8765"
    async with client.connect(uri) as ws:
        await asyncio.gather(consume(ws), produce(ws))


if __name__ == "__main__":
    asyncio.run(main())
