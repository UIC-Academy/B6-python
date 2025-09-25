"""
Count Words
"""

s = input("Enter string: ")
cnt = 0

s = s.strip()

print(s)

for i in range(0, len(s) - 1):
    if s[i] == ' ' and s[i+1] != ' ':
        cnt += 1

print(cnt + 1)