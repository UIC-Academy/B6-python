s = input("Enter sentence: ")


freq = dict()

print(s.split())

for word in s.split():
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)


dc = {
    (1, frozenset({11,2,3}), 3): "list"
}
