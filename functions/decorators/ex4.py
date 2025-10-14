def decorator(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        print(ret.upper())
    
    return wrapper


@decorator
def say_hi(s: str):
    return "Hi " + s

say_hi("Eshmat")