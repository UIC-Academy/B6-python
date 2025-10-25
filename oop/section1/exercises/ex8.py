from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return self.radius**2 * pi
    
    def length(self):
        return 2*pi*self.radius
    

c1 = Circle(
    radius=5
)

print(c1.length(), c1.area())