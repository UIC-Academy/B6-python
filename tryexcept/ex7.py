from typing import Callable

def decorator(
    func: Callable
):
    def wrapper(*args, **kwargs):
        try:
            print("Function is being called...")
            func(*args, **kwargs)
            print("Function success!")
        except Exception as e:
            print("Calling function has exception:", e)

    return wrapper


@decorator
def f():
    print(1/0)
    
f()