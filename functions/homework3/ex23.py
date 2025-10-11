users = [
    ("Eshmat", 20),
    ("Toshmat", 21),
    ("Gulchapchap", 19),
]


lst = list(map(lambda x: x[0], users))
lst2 = list(map(lambda x: x[1], users))

print(lst, lst2)