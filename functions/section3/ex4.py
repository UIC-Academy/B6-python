from typing import Callable

def upperize(s: str):
    return s.upper()

def process_string(
    s: str, 
    func: Callable
):
    return func(s)


string = "eshmat"
print(process_string(string, upperize))