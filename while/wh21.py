"""
Count Vowels
"""


string = input("Enter string: ")

vowels = "aeiou"

i = 0
cnt = 0
while (i < len(string)):
    if (string[i] in vowels):
        cnt += 1
    i += 1

print("Number of vowels:", cnt)