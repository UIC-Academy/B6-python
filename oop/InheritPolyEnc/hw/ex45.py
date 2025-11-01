"Create a class Point with __add__ to support vector addition."

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        new_point = Point(
            x=self.x+other.x, 
            y=self.y+other.y
        )
        return new_point
        
    def __str__(self):
        return f"Point<{self.x}, {self.y}>"
        

p1 = Point(x=1, y=0)
p2 = Point(x=3, y=-1)
resp = p1+p2
print(resp)

"""
A(1,0)
B(3,-1)
C(4,-1)

"""