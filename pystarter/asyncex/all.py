import asyncio
from typing import Any


async def foo(n: int) -> str:
    await asyncio.sleep(2)
    return f"n: {n}!"


def bar():
    f = asyncio.Future[Any]()
    f.set_exception(ValueError("bar"))
    return f


async def main():
    tasks = [foo(1), foo(2), foo(3), bar()]
    try:
        results = await asyncio.gather(*tasks, return_exceptions=True)
        print(results)
    except Exception as e:
        print(e)


asyncio.run(main())
