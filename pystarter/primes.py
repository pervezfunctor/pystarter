from typing import Iterable, Optional
from functools import reduce
from operator import add

from pydantic import validate_arguments


@validate_arguments
def is_prime(n: int) -> int:
    """Checks if n is prime. n should be >= 2"""

    assert n >= 2
    return not any((n % i == 0) for i in range(2, n))


@validate_arguments
def primes(start: int, stop: Optional[int] = None) -> Iterable[int]:
    """returns all primes between start and stop. start is optional, will be treated as 2"""

    if stop is None:
        stop = start
        start = 2

    for i in range(start, stop):
        if is_prime(i):
            yield i


@validate_arguments
def sum_of_primes(start: int, stop: Optional[int] = None) -> int:
    """sum of all primes between start and stop. start is optional, will be treated as 2"""

    return reduce(add, primes(start, stop), 1)
