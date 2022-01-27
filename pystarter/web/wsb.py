#!/usr/bin/env python

import asyncio
import json
import logging
from websockets.server import serve, WebSocketServerProtocol
from websockets.legacy.protocol import broadcast

logging.basicConfig()

USERS: set[WebSocketServerProtocol] = set()

value = 0


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


def broadcast_users_event():
    broadcast(USERS, users_event())


def value_event():
    return json.dumps({"type": "value", "value": value})


def broadcast_value_event():
    broadcast(USERS, value_event())


async def counter(websocket: WebSocketServerProtocol):
    global USERS, value

    try:
        USERS.add(websocket)
        broadcast_users_event()
        await websocket.send(value_event())

        async for message in websocket:
            event = json.loads(message)
            if event["action"] == "minus":
                value -= 1
                broadcast_value_event()
            elif event["action"] == "plus":
                value += 1
                broadcast_value_event()
            else:
                logging.error("unsupported event: %s", event)
    finally:
        # Unregister user
        USERS.remove(websocket)
        broadcast(USERS, users_event())


async def main():
    async with serve(counter, "localhost", 6789):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
