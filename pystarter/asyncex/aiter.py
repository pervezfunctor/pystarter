import asyncio
from typing import IO, AsyncIterable


class Reader(AsyncIterable[str]):
    file: IO[str]

    def __init__(self, filename: str):
        self.file = open(filename, "r")

    async def readline(self) -> str:
        return await asyncio.get_running_loop().run_in_executor(
            None, self.file.readline
        )

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val == "":
            raise StopAsyncIteration
        return val


async def main():
    reader = Reader("pyproject.toml")
    iter = reader.__aiter__()

    while True:
        try:
            line = await iter.__anext__()
            print(line)
        except StopAsyncIteration:
            break


if __name__ == "__main__":
    asyncio.run(main())
