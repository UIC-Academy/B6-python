try:
    f = open("binar", "xb")
    print("Binary file is being created...")
    f.close()
except FileExistsError:
    print("File already exists, continuing...")


f = open("binar", "wb")

f.write(bytes([100, 111, 124, 123, 218, 197]))

f.close()