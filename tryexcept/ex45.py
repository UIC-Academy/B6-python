def convert_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            func()
        except KeyError as e:
            raise ValueError(e)
    
    return wrapper
        

@convert_exceptions
def myfunc():
    d = {"hello": 1, "hi": 12}
    
    print(d["key1"])
    

myfunc()