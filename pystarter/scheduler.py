from typing import Generator


def do_work():
    print("Doing work")
    yield
    print("do more work")
    yield
    print("done")


def do_better_work():
    print("Doing better work")
    yield
    print("do more better work")
    yield
    print("done")


def scheduler(*coros: Generator[None, None, None]) -> None:
    for coro in coros:
        coro.send(None)

    for coro in coros:
        coro.send(None)

    try:
        for coro in coros:
            coro.send(None)
    except StopIteration:
        pass


scheduler(do_work(), do_better_work())
