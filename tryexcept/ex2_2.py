def invert(
    l: list[int]
):
    res = []
    for i in range(0, len(l)):
        try:
            res.append(l[i]**(-1))
        except ZeroDivisionError:
            print(f"l[{i}] = 0 ekan, tashlab ketyapman")
            continue
        
    return res


print(invert([1,2,3,4,5]))
print(invert([0,0,1,1,0]))