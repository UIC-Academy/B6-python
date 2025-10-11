from typing import Callable

def repeater(
    func: Callable, 
    n: int
) -> Callable:
    def inner():
        for _ in range(n):
            func()
        return "Success"
        
    return inner()

# repeater_10 = repeater(lambda : print("Hello"), 10)

print(repeater(lambda : print("Hello"), 10))