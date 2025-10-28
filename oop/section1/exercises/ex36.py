class Cat:
    def __init__(self, name):
        self.name = name

class Dog:
    def __init__(self, name):
        self.name = name    


c1 = Cat("Pishak")
d1 = Dog("Bobik")

print(isinstance(c1, Dog), isinstance(c1, Cat))