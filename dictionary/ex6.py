d: dict = {"name": "Eshmat", "age": 67, "city": "Samarqand"}

if "name" in d.keys():
    print(True)

if "Eshmat" in d.values():
    print(True)

print(d.keys())
print(d.values())
print(d.items())


# Tuple unpacking
for key, val in d.items():
    print(key, val)


tp = (1, 2)
a, b = tp
print(a, b)
