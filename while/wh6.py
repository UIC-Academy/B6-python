"""
User Input Loop: Prompt the user to enter a number and keep asking until they enter 0.
"""

while True:
    num = int(input("Enter number: "))

    if num == 0:
        break

    print("User entered:", num)
