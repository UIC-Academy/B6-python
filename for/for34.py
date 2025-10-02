"""
Find Common Divisors
"""

a, b = map(int, input().split())
s = 0


mn = min(a, b)

for i in range(mn, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break
