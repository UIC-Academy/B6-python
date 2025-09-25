"""
Tot samiy Fibonacci
"""

f1, f2 = 1, 1

print(f1, f2, end=" ")

for i in range(2, 10):
    tmp = f2
    f2 = f2 + f1
    f1 = tmp
    print(f2, end=" ")

print()