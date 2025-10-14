def decorator(func):
    def wrapper(*args, **kwargs):
        t = args[0]
        sorted_ = sorted(t)
        func(tuple(sorted_))
        
    return wrapper


@decorator
def myfunc(itrb: list[int] | tuple[int]):
    print("nums", itrb)
    
myfunc((1,2,2,3,5,1))