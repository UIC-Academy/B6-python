class Vehicle:
    def __init__(self, name, brand, color):
        self.name = name
        self.brand = brand
        self.color = color
    
    def move(self):
        print("Vehicle moving...")
        

class Car(Vehicle):
    def move(self):
        print("vmmmm....")
        
    
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
        

class PassengerCraft(Plane):
    def __init__(self, name, brand, color, passenger_capacity, is_comfort):
        self.passenger_capacity = passenger_capacity
        self.is_comfort = is_comfort
        super().__init__(name, brand, color)
        
    def take_off(self):
        print("Taking off...")