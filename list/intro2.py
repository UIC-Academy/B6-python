"""
Memory related points
"""

l1 = [3,2,4]
l2 = l1.copy()
l2.append(5)
print(l1, l2)

# print(l1.sort())
sorted_list = sorted(l1)
print(l1, sorted_list)

l1[0] = 10000
print(l1)