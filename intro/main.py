string = "O'zbekiston kelajagi buyuk davlat!"

print("buyuk" in string)
print(string[0:11])
print(string[:27])
print(string[-9:-2])

print(10 > 9, 11 < 9, 10 == 10)
print(bool("Eshmat"), bool(10), bool(-100))
print(bool(None))

print(7 ** 3)

x = 10
print(x < 5 and x < 10)
print(x < 5 or x < 11)
print(not x == 10)

grade: int = int(input("Enter grade: "))


if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade < 90:
    print("B")
elif grade >= 70 and grade < 80:
    print("C")
elif grade >= 60 and grade < 70:
    print("D")
elif grade >= 50 and grade < 60:
    print("E")
else:
    print("F")

print("Eshmat") if x > 10 else print("Toshmat")