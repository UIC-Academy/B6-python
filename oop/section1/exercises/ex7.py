class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calc_perimeter(self):
        return (self.height + self.width) * 2
    
    def calc_area(self):
        return self.width * self.height
    

r1 = Rectangle(
    width=5,
    height=7
)

print(r1.calc_perimeter())
print(r1.calc_area())

print(r1)