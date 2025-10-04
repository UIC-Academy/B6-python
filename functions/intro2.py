"""
Optional Arguments
"""

def f(x: int = 0, y: str = None) -> None:
    print(x, y)

f()
f(3)
f(3,"Hello")
f(3,"Hello")


"""
args and kwargs in Python

*args - Positional Arguments
**kwargs - Keyword Arguments
"""

def f2(*args, **kwargs):
    print(args)
    print(kwargs)
    return kwargs

print(f2())