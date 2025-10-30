class Vehicle:
    def __init__(self, name, brand, color):
        self.name = name
        self.brand = brand
        self.color = color
    
    def move(self):
        print("Vehicle moving...")
        

class Plane(Vehicle):
    def move(self):
        print("flying...")
        

class Aircraft(Plane):
    def __init__(self, name, brand, color, weapon_capacity, target_accuracy):
        self.weapon_capacity = weapon_capacity
        self.target_accuracy = target_accuracy
        super().__init__(name, brand, color)
    
    def bomb(self):
        print("Bombing the enemies...")
        
v = Vehicle(
    name="Afrosiyob",
    brand="Afrosiyob",
    color="white"
)

boieng = Plane(
    name="Boing",
    brand="Boing",
    color="white"
)

f16 = Aircraft(
    name="F16",
    brand="",
    color="black",
    weapon_capacity=10000,
    target_accuracy=97
)


print(v.__class__.__name__)
print(boieng.__class__.__name__)
print(f16.__class__.__name__)
print(Aircraft.__mro__)