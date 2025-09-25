"""
Prime Number Checker
"""

num = int(input("Enter prime number: "))
is_prime = True

i = 2
while (i <= num**0.5):
    if (num % i == 0):
        is_prime = False
        break

    i += 1

print("Prime" if is_prime else "Compound")