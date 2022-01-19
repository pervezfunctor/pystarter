import asyncio
import concurrent.futures


def blocking_io():
    with open("/dev/urandom", "rb") as f:
        return f.read(100)


def cpu_bound():
    return sum(i * i for i in range(10 ** 7))


async def main():
    loop = asyncio.get_running_loop()

    result = await loop.run_in_executor(None, blocking_io)
    print("default thread pool", result)

    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_io)
        print("custom thread pool", result)

    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound)
        print("custom process pool", result)


asyncio.run(main())
