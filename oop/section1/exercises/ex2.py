class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return f"Person<name={self.name}, age={self.age}>"
    
    
p1 = Person("Eshmat", 20)
print(p1)