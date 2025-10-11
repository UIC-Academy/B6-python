from typing import Callable


def apply(func: Callable, val: int) -> int:
    return func(val)


print(apply(lambda x: x**2, 5))