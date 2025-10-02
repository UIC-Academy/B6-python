"""
Secret Number: Use a while loop to let the user guess a secret number (e.g., 7). Print "Too high!" or "Too low!" until they guess correctly.
"""

secret = int(input("enter secret num: "))
while True:
    num = int(input("enter guessed num: "))
    if num > secret:
        print("too high")
    elif num < secret:
        print("too low")
    else:
        print(f"you are right {secret}")
        break
