from types import TracebackType
from typing import AsyncContextManager, Type
import asyncio


async def hello():
    return "hello from async context manager"


class ACM(AsyncContextManager[str]):
    async def __aenter__(self):
        print("aenter")
        msg = await hello()
        return msg

    async def __aexit__(
        self,
        __exc_type: Type[BaseException] | None,
        __exc_value: BaseException | None,
        __traceback: TracebackType | None,
    ):
        print("aexit")
        return True


async def acm():
    async with ACM() as msg:
        print(msg)


if __name__ == "__main__":
    asyncio.run(acm())
