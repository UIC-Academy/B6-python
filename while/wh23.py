"""
String reverse
"""


string = input("Enter string: ")
res = ""
i = len(string) - 1

while (i >= 0):
    res += string[i]
    i -= 1

print(res)
print(res == string)