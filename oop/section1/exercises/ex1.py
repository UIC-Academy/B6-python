class Car:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model
        
    def __str__(self) -> str:
        return f"Car<name={self.model}>"
    

c1 = Car(
    brand="Chevrolet",
    model="Damas"
)
c2 = Car(
    brand="Chevrolet",
    model="Matiz"
)

print(c1, c2)