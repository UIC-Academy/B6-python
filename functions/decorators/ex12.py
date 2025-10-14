def decorator(func):
    def wrapper(*args, **kwargs):
        l = args[0]
        l = list(set(l))
        func(l)
        
    return wrapper


@decorator
def myfunc(lst: list[int]):
    print("nums", lst)
    print("max is", max(lst))
    
myfunc([1,2,2,3,5,1])