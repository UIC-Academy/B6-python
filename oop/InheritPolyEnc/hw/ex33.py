class Shape:
    def area(self):
        raise NotImplementedError("not implemented")
    
class Rectangle(Shape):
    def __init__(self,width,heigh):
        self.width=width
        self.heigh=heigh
        
    def area(self):
        return self.width*self.heigh
    
class Circle(Shape):
    def __init__(self,r):
        self.r=r
        
    def area(self):
        import math
        return math.pi*self.r**2
    
r=Rectangle(4,5)
c=Circle(4)
v=Shape()

print(r.area())
print(c.area())
print(v.area())