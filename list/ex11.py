import sys

l = ["olma", "nok", "behi", "shaftoli", "banan"]

print(sys.getsizeof(l))

l.insert(1, "mango")
deleted = l.pop()
l.remove("olma")

print("Deleted fruit: ", deleted)
print(l)

l.clear()

print(l, sys.getsizeof(l))