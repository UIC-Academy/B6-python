from typing import Callable

def compose_funcs(
    funcs: list[Callable],
    val: int
):
    res = val
    for func in funcs:
        res = func(res)
    
    return res

f1 = lambda x: x**2
f2 = lambda x: x*5
f3 = lambda x: x//7

print(compose_funcs([f1, f2, f3], 100))