from typing import Callable

def operate(a: int, b: int, op: Callable):
    return op(a, b)

add = lambda x, y: x+y
sub = lambda x, y: x-y
mul = lambda x, y: x*y
div = lambda x, y: x//y

print(operate(5, 3, add))
print(operate(55, 6, div))
