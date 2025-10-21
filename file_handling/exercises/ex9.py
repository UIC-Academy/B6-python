try:
    open("files/hello.txt", "x")
except FileExistsError:
    print("File exists, continue...")

f = open("files/hello.txt", "r")

text = f.read()
print(text)

print("eshmat" in text)

f.close()