import sys

d: dict = {"name": "Eshmat", "age": 67, "city": "Samarqand"}
print(sys.getsizeof(d))

print(d.get("namee"))

d["occupation"] = "pensiyada"
d["phone"] = "+998001112233"
d["hobbies"] = ["football", "chess"]
# d["email"] = "eshmat@gmail.com"
d.update({"age": 70})
print(d, sys.getsizeof(d))

print(sys.getsizeof(dict()))

d.pop("city")

print(d)
