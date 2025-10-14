def decorator(func):
    def wrapper(s: str):
        if s == "":
            print("Can't give empty string as argument")
            return
        
        func(s)
        
    return wrapper


@decorator
def myfunc(s: str):
    print(f"Hello {s}!")
    
myfunc("")
myfunc("Eshmaty")