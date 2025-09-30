l = [1,2,4,6,2,6,8,9]

res = []


for i in l:
    if i not in res:
        res.append(i)

print(res)