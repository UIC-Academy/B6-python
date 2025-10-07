words = []


# print(" ".join(words))


def build_sentence(*words, sep=" "):
    return sep.join(words)
    # res = ""
    # for word in words:
    #     res += word + sep
    
    # return res[:-1]
    
res = build_sentence("Hello", "Eshmat", "how", "are", "you", sep="-")

print(res)