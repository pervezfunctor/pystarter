import asyncio
import random
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def return_after_5_secs(message: str):
    sleep(5)
    return message


pool = ThreadPoolExecutor(3)


async def do_it():
    identify = random.randint(1, 100)
    future = pool.submit(return_after_5_secs, (f"result: {identify}"))
    awaitable = asyncio.wrap_future(future)
    print(f"waiting result: {identify}")
    return await awaitable


async def main():
    tasks = [do_it(), do_it()]

    result = await asyncio.gather(*tasks)
    print(result)


print("waiting app")
