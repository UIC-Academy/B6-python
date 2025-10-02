"""
Su li fa o'yini
"""

import random

choices = ["tosh", "qaychi", "qog'oz"]

while True:
    comp_choice = random.choice(choices)
    user_choice = input("Enter your choice: ")

    if user_choice not in choices:
        print("Faqatgina tosh, qaychi va qog'oz deb kirita olasiz.")
    if user_choice == comp_choice:
        print("Bir xil narsa tanladingiz.")
        continue

    if comp_choice == "tosh" and user_choice == "qog'oz":
        print("User wins")
        break
    elif comp_choice == "tosh" and user_choice == "qaychi":
        print("Computer wins")
        break
    elif comp_choice == "qaychi" and user_choice == "tosh":
        print("User wins")
        break
    elif comp_choice == "qaychi" and user_choice == "qog'oz":
        print("Computer wins")
        break
    elif comp_choice == "qog'oz" and user_choice == "qaychi":
        print("User wins")
        break
    elif comp_choice == "qog'oz" and user_choice == "tosh":
        print("Computer wins")
        break
