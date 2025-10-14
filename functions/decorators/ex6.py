from typing import Callable

def decorator(func: Callable):
    def wrapper(n: int):
        if n < 0:
            print("You can't pass negative number as argument.")
            return
        func(n)
    return wrapper

@decorator
def myfunc(name: int):
    print(f"Positive, {name}")

myfunc(-1)
myfunc(5)
