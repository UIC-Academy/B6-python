from typing import Callable

def func_name_print(f: Callable):
    print(f.__name__)
    print(f(5))
    

def greet(x: int):
    return f"{x} Hello World"
    
add = lambda x: x**3

func_name_print(greet)
func_name_print(add)