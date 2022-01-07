from typing import Iterable


def fibo() -> Iterable[int]:
    lo = 1
    hi = 1
    while True:
        yield lo
        hi = hi + lo
        lo = hi - lo
