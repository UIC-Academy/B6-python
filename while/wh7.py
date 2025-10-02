"""
Positive Numbers Only: Ask the user for a number. If it's negative, ask again. Keep asking until a positive number is entered.
"""

while True:
    num = int(input("Enter num: "))

    if num > 0:
        print("User entered positive number.")
        break
