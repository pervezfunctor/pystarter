import asyncio
from asyncio import Future


async def foo(fut: asyncio.Future[str]):
    await asyncio.sleep(2)
    fut.set_result("foo")


async def main():
    fut = Future[str]()
    asyncio.create_task(foo(fut))
    result = await fut
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
