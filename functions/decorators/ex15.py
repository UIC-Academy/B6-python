def check_negative(func):
    def wrapper(*args, **kwargs):
        for n in args:
            if (n <= 0):
                print("Warning: Negative number detected.")
                return
        
        func(*args)
        
    return wrapper
    
@check_negative
def myfunc(*args):
    print(args)
    

myfunc(1,2,3,4,1)
myfunc(1,2,3,4,-1)