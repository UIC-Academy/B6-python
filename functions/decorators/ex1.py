from typing import Callable
from datetime import datetime, timezone
import time


def decorator(
    func: Callable
):
    def wrapper(*args, **kwargs):
        print("Starting...")
        time.sleep(2)
        func(*args, **kwargs)
        print("Done!")
        
    return wrapper

@decorator
def myfunc(a: int, parent: int = None):
    print(datetime.now(timezone.utc))
    print(a, parent)
    
myfunc(5, parent=6)