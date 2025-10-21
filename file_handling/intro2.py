f = open("test.txt", "a+")

print(f.read())

f.seek(0)

print(f.tell())
f.write("This is append mode!\t")
print(f.tell())

f.seek(0)
print(f.read())

f.close()