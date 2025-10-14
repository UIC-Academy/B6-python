"""
Decorator Definition: changing the behaviour of the function without changing the function
"""


def logger(func):
    def wrapper(*args, **kwargs):
        # check if authenticated
        print("Before function")
        func()
        print("After function")
        # function completed at time.Now()
    
    return wrapper

@logger
def f():
    print("Hello")

f()
    
# resf = logger(f)
# print(resf)
# resf()