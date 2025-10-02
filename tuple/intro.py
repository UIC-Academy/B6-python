import sys

mytup = (
    1,
    2,
    3,
    True,
    False,
)
l = [1, 2, 3]

print(sys.getsizeof(mytup), sys.getsizeof(l))
print(mytup.count(0), mytup.index(1))

print(list(mytup), mytup)


l = [1, ["salom", "dunyo"], True]
t = (1, ["hello", "world"], False)

print(t)
t[1][1] = "world2"
# t[1] = ["hello2", "world2"]  this does not work!
print(t)

if 1 in t:
    print("True")

print(
    (
        1,
        2,
    )
    * 3
)
