def student_info(name, age, **details):
    info = f"Name: {name}, Age: {age}"
    
    if details:
        for key, value in details.items():
            info += f", {key}: {value}"
    
    return info


print(student_info("Eshmat", 19))
print(student_info("Toshmat", 20, workplace="UIC Group", hobbies="football, chess"))