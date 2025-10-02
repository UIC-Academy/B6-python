s = input("Enter string: ")


freq = dict()

for c in s:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

print(freq)