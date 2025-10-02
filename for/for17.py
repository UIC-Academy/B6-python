"""
Check For Uppercase
"""

s = input("Enter string: ")
is_upper = False

for c in s:
    if c.isupper():
        is_upper = True


print(is_upper)
