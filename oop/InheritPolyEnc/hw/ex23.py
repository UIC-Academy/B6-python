class Animal:
    def live(self):
        print("Animal is living...")

class Flyer(Animal):
    def move(self):
        print("Flyer flies...")
        

class Swimmer(Animal):
    def move(self):
        print("Swimmer swims...")
        
        
class Goose(Swimmer, Flyer):
    pass

g = Goose()
g.move()
print([clss.__name__ for clss in Goose.mro()])