class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def move(self, x = 0, y = 0, z = 0):
        self.x += x
        self.y += y
        self.z += z
    
    @classmethod
    def explain(cls):
        print("The Point class is a base construct to build Point objects over 3D system.")
    
    @staticmethod
    def generate_id():
        import uuid
        return uuid.uuid4()

    def __repr__(self):
        return f"Point<{self.x},{self.y},{self.z}>"
    
    # def __str__(self):
    #     return f"X = {self.x}, Y={self.y}, Z = {self.z}"
    
def generate_id():
    pass

p1 = Point(0,1,0)
p2 = Point(1,-2,4)
p1.move(1,4,-8)
p2.move(-1,3,-2)

print(Point.generate_id())

print(p1, p2)


"""
3 xil method turlari bor:
- object method (aynan o'sha mahsulotga tegishli funksionallik, jarayon)
- class method (butun class (zavod) ga tegishli jarayon)
- static method (hech qaysiga tegishli emas, shunchaki utility)
"""

