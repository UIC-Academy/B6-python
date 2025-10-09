from typing import Callable
import time

def greet():
    print("Salom Eshmat!")

def exec_twice(
    func: Callable
):
    print("Shu odam request jonatdi", time.time())
    func()

exec_twice(greet)
