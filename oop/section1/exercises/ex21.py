class Car:
    cnt = 0
    
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color
        Car.cnt += 1
    
    def __str__(self):
        return self.name

    def __del__(self):
        Car.cnt -= 1
        del self
        
    @classmethod
    def explain(cls):
        print("This is GM!")
    

c1 = Car("Nexia 2 legenda", 5000, "white")
c2 = Car("Onix tufta", 17000, "black")
c3 = Car("Maluba", 30000, "purple")

print(Car.cnt)
print(Car.explain())

del c2

print(Car.cnt)