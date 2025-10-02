students = {
    "eshmat": {
        "math": 45,
        "science": 60,
        "history": 78
    },
    "toshmat": {
        "math": 56,
        "science": 78
    }
}

for name, grades in students.items():
    sm = 0
    for _, grade in grades.items():
        sm += grade
    
    print(name, sm/len(grades))


res = {name: sum(grade for grade in grades.values())/len(grades.keys()) for name, grades in students.items()}
print(res)

print(len(students))


st2 = students.copy()

st2.pop("eshmat")
print(students, st2)

print(students.get("gishmat", 14))