import asyncio


async def foo(n: int):
    await asyncio.sleep(4)
    print(f"n: {n}!")


async def main():
    try:
        await asyncio.wait_for(foo(1), timeout=2)
    except asyncio.TimeoutError:
        print("timeout!")


asyncio.run(main())
