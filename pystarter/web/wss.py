#!/usr/bin/env python

import asyncio
from websockets import server

server_fut = asyncio.Future[None]()


async def hello(websocket: server.WebSocketServerProtocol, path: str) -> None:
    name = await websocket.recv()
    if name == "quit":
        server_fut.set_result(None)

    print(f"<<< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main():
    async with server.serve(hello, "localhost", 8765):
        await server_fut


if __name__ == "__main__":
    asyncio.run(main())
