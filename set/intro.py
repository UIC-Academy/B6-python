s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {1, 2}

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)
print(s3 <= s1)

# union - birlashma
# intersection - kesishma
# difference - ayirma

s1.add("gishmat")
print(s1)
s1.remove("gishmat")
print(s1)
s1.pop()
print(s1)
