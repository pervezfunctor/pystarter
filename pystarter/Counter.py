from typing import Iterable


class Counter(Iterable[int]):
    count: int = 0

    def __init__(self, stop: int = 0):
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.stop:
            raise StopIteration

        result = self.count
        self.count += 1
        return result


def counter(stop: int) -> Counter:
    return Counter(stop)


def counting(stop: int) -> Iterable[int]:
    count = 0
    while count < stop:
        yield count
        count += 1
