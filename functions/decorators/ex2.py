from typing import Callable
import time

def decorator(func: Callable):
    count = 0
    def wrapper(*args, **kwargs):        
        nonlocal count
        count+=1
        func(*args, **kwargs)
        print("Call count:", count)
    return wrapper

@decorator
def myfunc():
    print("I am a function!")

myfunc()
myfunc()
