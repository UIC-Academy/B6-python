from typing import Callable


def apply_all(
    funcs: list[Callable],
    value: int
):
    return [func(value) for func in funcs]


print(apply_all(
    [lambda x: x + 1, lambda x: x * 2],
    3
))