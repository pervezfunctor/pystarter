import asyncio


async def foo():
    await asyncio.sleep(10)
    print("Foo!")
    return 100


# async def hello_world():
#     task = asyncio.create_task(foo())
#     print(task)
#     await asyncio.sleep(5)
#     print("Hello World!")
#     await asyncio.sleep(10)
#     print(task)


def do_some_computation():
    pass


async def hello_world():
    x = asyncio.create_task(foo())  # Task <- Future
    y = asyncio.create_task(foo())
    do_some_computation()
    z = foo()
    print(await asyncio.gather(x, y, z))


asyncio.run(hello_world())
