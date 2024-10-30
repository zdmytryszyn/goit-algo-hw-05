from typing import Generator, Callable


def generator_numbers(text: str) -> Generator:

    for word in text.split():
        if word.strip()[0].isdigit():
            yield float(word.strip())


def sum_profit(text: str, func: Callable) -> float:
    return sum(profit for profit in func(text))
