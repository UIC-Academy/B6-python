l = [1,2,3,4, True, "eshmat"]
t = (1,2,3,4, True, "eshmat")
st = {1,2,3,4,5}

l.insert(2, "hello")
l.pop(3)
l.remove("eshmat")
print(l)

l.reverse()
print(l)

nums = [4,2,4,6,1,7,8,10, 5.6, True, False]
nums.sort(reverse=True)
print(nums)