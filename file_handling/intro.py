f = open("files/test.txt", "r+")

print("Cursor pos:", f.tell())

res = f.read()
print(len(res))

print("Cursor pos:", f.tell())

f.seek(0)

f.write("Men yozaman!\n\n")

print("Cursor pos:", f.tell())

f.seek(0)

print(f.read())

print("Cursor pos:", f.tell())

f.close()
