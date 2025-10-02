"""
Write a program that counts down from 10 to 1.
"""

is_increasing = bool(input("O'ssinmi kamaysinmi? (1/0)"))
i = float(input("Enter i: "))
j = float(input("Enter j: "))
jmp = float(input("Enter jmp: "))

if is_increasing == True:
    if i > j:
        print("i j dan katta bo'la olmaydi, agar o'sishni tanlagan bo'lsangiz.")

    while i <= j:
        print(i)
        i += jmp
else:
    if i < j:
        print("i j dan kichik bo'la olmaydi, agar kamayishni tanlagan bo'lsangiz.")

    while i >= j:
        print(i)
        i -= jmp
