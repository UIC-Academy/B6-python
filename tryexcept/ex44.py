def validate_args(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        for i in args:
            if not isinstance(i, int):
                raise TypeError("Given number isn't integer.")
    return wrapper


@validate_args
def myfunc():
    print("All number is integer.")

myfunc()
