def exception_log(func):
    def wrapper(*args, **kwargs):
        try:
            func()
        except Exception as err:
            print(f"Error type: {type(err)}:", err)
        
    return wrapper

@exception_log
def myfunc():
    n = int(input("Enter n:"))
    if n == 1:
        raise PermissionError("This is permission error")
    elif n == 2:
        raise TypeError("Mismatching types")
    elif n == 3:
        raise IndexError("Index out of range")
    elif n == 4:
        raise KeyError("This key is not yours")
    else:
        raise Exception("Any other error")

myfunc()