import asyncio


async def foo(fut: asyncio.Future[str]):
    await asyncio.sleep(2)
    fut.set_result("foo")


async def main():
    fut = asyncio.Future[str]()
    asyncio.create_task(foo(fut))
    result = await fut
    print(result)


loop = asyncio.new_event_loop()

loop.run_until_complete(main())
