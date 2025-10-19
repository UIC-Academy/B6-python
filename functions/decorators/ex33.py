import time
from datetime import datetime, UTC, timedelta


def cache_time(func):
    cached_result = 0
    last_cached_time = None
    def wrapper(*args, **kwargs):
        nonlocal cached_result
        nonlocal last_cached_time
        
        if last_cached_time and (datetime.now(UTC) - last_cached_time) <= timedelta(seconds=5):
            return cached_result
        
        res = func(*args, **kwargs)
        cached_result = res
        last_cached_time = datetime.now(UTC)
        
        return cached_result
    
    return wrapper


@cache_time
def calculate():
    print("Calculating result...")
    time.sleep(5)
    result = 100.15
    
    return result


print(calculate())
print("Sleeping for 2 seconds...")
time.sleep(2)
print(calculate())
print("Sleeping for 7 seconds...")
time.sleep(7)
print(calculate())