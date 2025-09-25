"""
Check for Positives
"""

NUMBERS = 5

for i in range(NUMBERS):
    n = int(input("Enter n: "))

    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
