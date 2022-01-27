import asyncio


async def foo():
    print("Running in foo")
    await asyncio.sleep(0)
    print("Explicit context switch to foo again")
    await asyncio.sleep(0)
    print("foo again")


coro = foo()

coro.send(None)
coro.send(None)
coro.throw(asyncio.CancelledError)
