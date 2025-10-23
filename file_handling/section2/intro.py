# f = open("file.txt", "r")

# f.close()


with open("file.txt", "r+") as f:
    f.write("Hello World!\n")

print("File closed? ", f.closed)