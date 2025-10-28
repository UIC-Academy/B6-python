class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    @classmethod
    def create_from_diameter(cls, diameter):
        return Circle(radius=diameter/2)
    
    def __repr__(self):
        return f"Circle<r={self.radius}>"
    
    @staticmethod
    def is_even(n: int):
        return n % 2 == 0


c1 = Circle.create_from_diameter(10)

print(c1)
print(Circle.is_even(4))


class MathUtils:
    def add(a, b):
        return a+b
    
    def mul(a, b, c):
        return a * b * c
    
print(MathUtils.add(1,2))
print(MathUtils.mul(1,2,3))