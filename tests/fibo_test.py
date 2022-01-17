from pystarter.Fibo import Fibo
from itertools import islice


def test_fibo() -> None:
    fibo = islice(Fibo(), 10)
    assert tuple(fibo) == (1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
