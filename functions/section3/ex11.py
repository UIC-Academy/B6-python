"""
Lambda function = anonymous (nameless) functions
"""

def sqr(a):
    return a**2


def create_multiplier(n):
    return lambda x: x**2


multiplier_by_2 = create_multiplier(2)


print(multiplier_by_2(7))
print(multiplier_by_2)