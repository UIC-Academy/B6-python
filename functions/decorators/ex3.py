def decorator(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        func()
    
    return wrapper


@decorator
def salom():
    print("Salom!")
    
salom()