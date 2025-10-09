from typing import Callable


def kvadrat(a: int):
    return a**2

def apply_operation(
    x: int, 
    y: int, 
    operation: Callable
) -> int:
    reslist = [operation(x), operation(y)]
    return reslist


res = apply_operation(2,3, kvadrat)

print(res)
