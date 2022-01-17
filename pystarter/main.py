from typing import Iterable, Generator


def producer() -> Iterable[int]:
    for i in range(10):
        yield i + 1


def consumer() -> Generator[None, str, None]:
    yield
    for _ in range(10):
        x: str = yield
        print(x)


def producer_consumer() -> Generator[int, str, None]:
    for i in range(10):
        x: str = yield i + 1
        if x is not None:
            print(f"got: {x}")


def use_producer() -> None:
    for i in producer():
        print(i)


def use_consumer() -> None:
    c = iter(consumer())
    next(c)
    for i in range(10):
        c.send(str(i))


def use_producer_consumer() -> None:
    pc = producer_consumer()
    x = next(pc)
    for _ in range(9):
        print(f"sending: {x}")
        x = pc.send(str(x))


use_producer()
use_consumer()
use_producer_consumer()
