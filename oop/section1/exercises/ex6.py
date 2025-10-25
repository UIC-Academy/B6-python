class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hi, I am {self.name}!")
        

p1 = Person(name="Eshmat")

p1.introduce()