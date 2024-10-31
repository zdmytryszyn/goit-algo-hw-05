from typing import Generator, Callable


def generator_numbers(text: str) -> Generator:

    for word in text.split(" "):
        try:
            if f" {word} " in text:
                yield float(word)
        except ValueError:
            continue


def sum_profit(text: str, func: Callable) -> float:
    return sum(profit for profit in func(text))
