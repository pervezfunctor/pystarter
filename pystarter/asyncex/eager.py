import asyncio
from random import randrange


async def foo(n: str):
    s = randrange(5)
    print(f"{n} will sleep for: {s} seconds")
    await asyncio.sleep(s)
    return f"{n}!"


async def main():
    counter = 0
    tasks = [foo("a"), foo("b"), foo("c")]

    for future in asyncio.as_completed(tasks):
        n = "quickest" if counter == 0 else "next quickest"
        counter += 1
        result = await future
        print(f"the {n} result was: {result}")


asyncio.run(main())
