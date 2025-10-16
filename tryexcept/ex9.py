l1 = [10,15,20,25,30]
l2 = [2,3,0,5,6,7, 8, 9, 10]
res = []

maxlen = max(len(l1), len(l2))

for i in range(0, maxlen):
    try:
        res.append(l1[i] / l2[i])
    except IndexError:
        print(f"Ignored l[{i}]: Listlar uzunliklari turlicha ekan, uzun listdagi qolgan sonlarni ignore qilaman.")
        break
    except ZeroDivisionError:
        print(f"l[{i}] da 0 bor ekan, ignore qilaman.")

print(res)