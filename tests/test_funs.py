from pystarter.funs import fibo
from itertools import islice


def test_funs() -> None:
    assert list(islice(fibo(), 10)) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
