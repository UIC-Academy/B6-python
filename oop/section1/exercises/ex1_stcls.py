class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def create(cls, s: str):
        name, age = s.split(",")
        
        return Student(name=name, age=age)
    
    def __str__(self):
        return f"Student<{self.name}, {self.age}>"
    
st1 = Student("Anna", 12)
st2 = Student.create("Eshmat,90")

print(st1, st2)