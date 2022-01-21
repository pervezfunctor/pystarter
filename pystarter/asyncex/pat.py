import asyncio
from random import randrange


async def foo(n: int):
    try:
        s = randrange(5)
        print(f"{n} will sleep for: {s} seconds")
        await asyncio.sleep(s)
        print(f"n: {n}!")
        return n
    except asyncio.CancelledError:
        print(f"{n} was cancelled")
        raise


async def main():
    tasks = [foo(1), foo(2), foo(3)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for p in done:
        print(await p)
    for p in pending:
        p.cancel()


asyncio.run(main())
