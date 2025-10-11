products: dict = {
    "olma": 25,
    "apelsin": 60,
    "ananas": 100,
    "mandarin": 50,
    "nok": 30,
    "malina": 150
}

# Teacher's solution (inefficient)
lambda1 = lambda p: p[1] > 50
f = lambda pdict: print(list(filter(lambda1, pdict)))
f(products.items())

# for p in products.items():
#     if p[1] > 50:
#         print(p[0])


# Shaxriyor's solution (efficient, TOP TIER)
a = list(filter(lambda x: x[1] > 50, products.items()))
print(a)