import time

def our_cache(func):
    last_calls = dict()
    def wrapper(*args, **kwargs):
        nonlocal last_calls
        print(last_calls)
        s = args[0]
        if s in last_calls:
            time.sleep(1)
            return last_calls[s]
        else:
            res = func(s)
            if len(last_calls) > 2:
                last_calls.pop(list(last_calls.keys())[0])
            last_calls[s] = res
        
    return wrapper


@our_cache
def say_hi(s: str):
    print("Working...")
    time.sleep(4)
    return f"Hi {s}!"


print(say_hi("Eshmat"))
print(say_hi("Toshmat"))
print(say_hi("Gishmat"))
print(say_hi("Eshmat"))
print(say_hi("Gulchapchap"))
print(say_hi("Eshmat"))
print(say_hi("Gulchapchap"))
print(say_hi("Gishmat"))

# Hi Eshmat
# Hi Toshmat
# Hi Gishmat