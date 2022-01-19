import asyncio
import uvloop


async def foo():
    print("foo!")


async def foo_bar():
    await foo()
    print("bar")


uvloop.install()
asyncio.run(foo_bar())
