def exception_log(func):
    def wrapper(*args, **kwargs):
        try:
            func()
        except Exception:
            print("Error suppressed!")
        
    return wrapper


@exception_log
def myfunc():
    raise FileNotFoundError("Bunaqa fayl yoqku!")

myfunc()