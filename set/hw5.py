st1 = {1, 2, 3, 4}
st2 = {3, 4, 5, 6}


# print(st1.union(st2))
# print(st1.intersection(st2))

# UNION - hammasi
# INTERSECTION - ikkalasidayam bori
# DIFFERENCE - diff(st1, st2), diff(st2, st1)

# res = {}

# for i in st1:
#     st2.add(i)

res = set()

for i in st1:
    if i in st2:
        res.add(i)

print(st2)
print(res)
