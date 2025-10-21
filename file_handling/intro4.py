f = open("test.txt", "r+")

print(f.readline(5))
print(f.tell())
print(f.readline(8))
print(f.tell())

f.seek(0)

print(f.readlines())

l = ["\nwe\t", "are\t", "the\t", "champions\t"]

f.writelines(l)

f.close()