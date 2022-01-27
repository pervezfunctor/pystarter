#!/usr/bin/env python

import asyncio
from websockets import server


async def receive_count(websocket: server.WebSocketServerProtocol) -> None:
    async for cnt in websocket:
        greeting = f"Hello {cnt}!"
        print(f">>> {greeting}")
        await websocket.send(greeting)


async def main():
    async with server.serve(receive_count, "localhost", 8765):
        await asyncio.Future()


asyncio.run(main())
