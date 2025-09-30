students = ["eshmat", "toshmat", "gulchapchap", "gulpari"]

grades = [80, 79, 90, 78]


idx = students.index("eshmat")

print(grades[idx])


student_grades = {
    "eshmat": 80,
    "toshmat": 80,
    "gulchapchap": 90,
    "gulpari": 78,
    "gishmat": 10
}

student_grades["zafarbek"] = 95
student_grades["eshmat"] = 0

print(student_grades)

# student_grades.clear()
# print(student_grades)

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

print(student_grades.get("shaxriyor"))

popped = student_grades.pop("eshmat")
last_popped = student_grades.popitem()

print(last_popped, student_grades)

student_grades.setdefault("gishmat", 80)
if not "gishmat" in thisdict:
    thisdict["gishmat"] = 80

print(student_grades)