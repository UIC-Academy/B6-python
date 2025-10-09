from typing import Callable

def safe_divide(a: int, b: int) -> float:
    return a/b

def err_handler():
    return "0 ga bo'lish mumkin emas"

def run_if_safe(
    func: Callable,
    handler: Callable,
    a: int,
    b: int
):
    if (b != 0):
        return func(a, b)
    else:
        return handler()
        

print(run_if_safe(safe_divide, err_handler, 3, 0))
