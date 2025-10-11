def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b


ops: list = [add, sub]

for op in ops:
    a, b = map(int, input("Enter a, b: ").split(","))
    print(op(a, b))

