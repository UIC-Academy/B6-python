from typing import Callable

def mul_n(n: int) -> Callable:
    return lambda x: x * n

mul_5 = mul_n(5)
mul_100 = mul_n(100)

print(mul_5(20))
print(mul_100(6))