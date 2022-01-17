from typing import Iterable


class Fibo(Iterable[int]):
    lo: int = 0
    hi: int = 1

    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.lo, self.hi = self.hi, self.lo + self.hi
        return self.lo
