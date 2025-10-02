"""
Count Consonants
"""

vowels = "aeiou"

s = input("Enter string: ")
cnt = 0

for c in s:
    if c not in vowels and c.isalpha():
        cnt += 1

print("Number of consonants:", cnt)
