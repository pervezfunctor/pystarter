import asyncio
from typing import AsyncIterable, Callable
from aiter import Reader


def amap(
    func: Callable[[str], str], iterable: AsyncIterable[str]
) -> AsyncIterable[str]:
    return (func(v) async for v in iterable)


def afilter(
    pred: Callable[[str], bool], iterable: AsyncIterable[str]
) -> AsyncIterable[str]:
    return (v async for v in iterable if pred(v))


async def main():
    reader = Reader("pyproject.toml")
    iter = aiter(reader)

    filtered = afilter(lambda s: s.strip() != "", iter)
    mapped = amap(lambda s: s.upper(), filtered)

    s = ""
    async for line in mapped:
        s += line

    print(s)


if __name__ == "__main__":
    asyncio.run(main())
