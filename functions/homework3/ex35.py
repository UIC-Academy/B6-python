words = ["a", "able", "about", "across", "all", "always", "amaze", "answer", "any", "around"]


func = lambda f, l: [w for w in l if f(w)]

print(func(lambda w: len(w) < 4, words))

l = []
for word in words:
    if (len(word) < 4):
        l.append(word)
        
print(l)