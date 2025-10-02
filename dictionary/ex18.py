students = {
    "eshmat": {
        "math": 45,
        "science": 60
    },
    "toshmat": {
        "math": 56,
        "science": 78
    }
}


print(students.get("eshmat", None).get("science", None))

students["eshmat"].update({
    "history": 56
})

print(students)