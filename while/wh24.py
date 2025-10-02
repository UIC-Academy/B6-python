"""
Palindrome checker
"""

string = input("Enter string: ")

i, j = 0, len(string) - 1
is_palindrome = True

while i <= j:
    if string[i] != string[j]:
        is_palindrome = False
        break

    i += 1
    j -= 1

print("Palindrome" if is_palindrome else "Not palindrome")
