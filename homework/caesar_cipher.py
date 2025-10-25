k = int(input("Enter k: "))

s = input("Enter string: ")


res = ""

for char in s:
    if ord(char) >= 65 and ord(char) <= 90:
        sm = ord(char) + k
        if sm > 90:
            res += chr(sm - 26)
        else:
            res += chr(sm)
    elif ord(char) >= 97 and ord(char) <= 122:
        sm = ord(char) + k
        if (sm > 122):
            res += chr(sm - 26)
        else:
            res += chr(sm)
    else:
        res += char

print(res)