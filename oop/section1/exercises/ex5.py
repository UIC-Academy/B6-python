class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        
        print("New student created!")
        
    def __del__(self):
        print("Student is deleted!")
        
        
st1 = Student(
    name="Eshmat",
    age=19,
    id="su14209"
)

del st1