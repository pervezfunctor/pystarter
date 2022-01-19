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


async def proc(executor: Executor, value: int) -> int:
    fut = executor.submit(next_prime, value)
    return await asyncio.wrap_future(fut)


async def main():
    with ProcessPoolExecutor() as executor:
        values: list[int] = [30000000, 50000000, 100, 10000, 100000, 1000000]
        futs = [proc(executor, v) for v in values]
        for fut in asyncio.as_completed(futs):
            print(await fut)


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    e = time.perf_counter()
    print(f"{e - s:0.4f} seconds")
