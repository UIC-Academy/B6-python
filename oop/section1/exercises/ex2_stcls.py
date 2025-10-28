class Pet:
    cnt = 0
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        Pet.cnt += 1
        
    @classmethod
    def count(cls):
        return cls.cnt
    
p1 = Pet("Bobik", "black")
p2 = Pet("Tuzik", "black")
p3 = Pet("Reks", "red")

print(Pet.count(), Pet.cnt)