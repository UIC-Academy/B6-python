"""
Prime Number Check
"""

n = int(input("Enter n: "))
is_prime = True

for i in range(2, int(n ** (0.5)) + 1):
    if n % i == 0:
        is_prime = False
        break

print(is_prime)
