"""
Number Series Sum
"""
import math

n = int(input("Enter n: "))
sm = 0


for i in range(1, n+1):
    sm += 1/math.factorial(i)

print("Sum:", sm)