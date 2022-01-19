import time
from concurrent.futures import ProcessPoolExecutor


def is_prime(n: int) -> int:
    """Checks if n is prime. n should be >= 2"""

    assert n >= 2
    return not any((n % i == 0) for i in range(2, n))


def next_prime(start: int) -> int:
    while not is_prime(start):
        start += 1
    return start


def main():
    with ProcessPoolExecutor() as executor:
        values: list[int] = [30000000, 50000000, 100, 10000, 100000, 1000000]
        result = executor.map(next_prime, values)
        print(*result)


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    e = time.perf_counter()
    print(f"{e - s:0.4f} seconds")
