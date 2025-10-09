"""
Max of Three: kattasini 100 ga ko'paytirib chiqaring.
"""


def max_of_three(a: int, b: int, c: int) -> int:
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    elif c > a and c > b:
        return c


res = max_of_three(1,2,3)
print(res*100)