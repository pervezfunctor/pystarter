import asyncio
from concurrent.futures import Executor, ProcessPoolExecutor
import time


def is_prime(n: int) -> int:
    """Checks if n is prime. n should be >= 2"""

    assert n >= 2
    return not any((n % i == 0) for i in range(2, n))


def next_prime(start: int) -> int:
    while not is_prime(start):
        start += 1
    return start


async def one(executor: Executor) -> int:
    fut = executor.submit(next_prime, 30000000)
    return await asyncio.wrap_future(fut)


async def two(executor: Executor):
    fut = executor.submit(next_prime, 50000000)
    return await asyncio.wrap_future(fut)


async def main():
    with ProcessPoolExecutor() as executor:
        o = one(executor)
        t = two(executor)
        results = await asyncio.gather(o, t)
        print(*results)


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    e = time.perf_counter()
    print(f"{e - s:0.4f} seconds")
