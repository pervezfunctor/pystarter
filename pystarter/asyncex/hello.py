import asyncio


async def foo():
    print("foo!")


async def foo_bar():
    await foo()
    print("bar")


asyncio.run(foo_bar())
