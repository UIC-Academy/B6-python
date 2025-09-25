"""
String Reversal
"""

s = input("Enter string: ")
res = ""

for i in range(len(s)-1, -1, -1):
    res += s[i]
