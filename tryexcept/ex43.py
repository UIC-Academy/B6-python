from typing import Callable

def safe_call(func: Callable):
    def wrapper(*args, **kwargs):
        try:
            func()
        except ZeroDivisionError:
            print("Division by 0 is not allowed")
        except Exception as e:
            raise Exception(e)
        
    return wrapper


@safe_call
def myfunc():
    import random
    l = [ZeroDivisionError, FileNotFoundError, KeyError, TypeError]
    i = random.randrange(0, 3)
    
    raise l[i]

myfunc()