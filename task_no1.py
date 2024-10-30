from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    cache = {}

    def fibonacci(num: int) -> int:
        if num <= 1:
            return num
        elif num in cache.keys():
            return cache[num]
        cache[num] = fibonacci(num - 1) + fibonacci(num - 2)
        return cache[num]

    return fibonacci
