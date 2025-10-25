class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        
    def bark(self):
        print(f"{self.name}'s bark!!!")
        
    def __str__(self):
        return f"Dog<{self.name}>"

laycha = Dog(
    name="Bobik",
    age=7,
    color="qora"
)
laycha2 = Dog(
    name="Tuzik",
    age=10,
    color="white"
)

laycha.bark()
laycha2.bark()