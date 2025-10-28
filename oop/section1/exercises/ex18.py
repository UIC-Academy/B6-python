class Student:
    school = "Mirzo Ulug'bek Ixtisoslashtirilgan maktabi"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

st1 = Student("Eshmat", 19)
st2 = Student("Toshmat", 12)
print(st1.school, st2.school)