class Vehicle:
    def move(self):
        raise NotImplementedError("You are not a vehicle!")


class Car(Vehicle):
    pass
        

class Train(Vehicle):
    def move(self):
        print("puuuv...")

c = Car()
t = Train()

c.move()
t.move()