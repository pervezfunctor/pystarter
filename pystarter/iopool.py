import asyncio
from concurrent.futures import Executor, ThreadPoolExecutor
from contextlib import asynccontextmanager
from typing import (
    IO,
    AsyncIterable,
)


async def readlines(pool: Executor, stream: IO[str]) -> AsyncIterable[str]:
    while True:
        loop = asyncio.get_running_loop()
        line = await loop.run_in_executor(pool, stream.readline)
        if not line:
            break
        yield line


@asynccontextmanager
async def async_open(filename: str, max_threads: int = 100):

    pool = ThreadPoolExecutor(max_workers=1)
    loop = asyncio.get_event_loop()
    file = await loop.run_in_executor(pool, open, filename, "r")
    try:
        yield readlines(pool, file)
    finally:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(pool, file.close)
        pool.shutdown(wait=False)


async def read_all():
    async with async_open("pyproject.toml") as f:
        async for line in f:
            print(line)


if __name__ == "__main__":
    asyncio.run(read_all())
