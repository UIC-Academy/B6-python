from typing import Callable, Iterable

def isEven(a: int) -> bool:
    if not isinstance(a, int):
        return False
    
    return a % 2 == 0


juftmi = isEven

print(juftmi(5))
print(isEven, id(isEven))

# a, b = map(int, input().split())


l = [1,2,3, 5.0]
print(list(map(lambda x: x**2, l)))


def mymap(
    operation: Callable,
    collection: Iterable
) -> int:
    res = []
    for item in collection:
        res.append(operation(item))
    
    return res

print(mymap(lambda x: x**2, l))
print(list(filter(lambda x: x % 2 == 0, l)))

def myfilter(
    operation: Callable,
    collection: Iterable
) -> int:
    res = []
    for item in collection:
        if operation(item):
            res.append(item)
    
    return res

print(myfilter(lambda x: isinstance(x, int), l))