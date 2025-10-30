class Person:
    def __init__(self, name, age, passport, jshshir):
        self.name = name
        self.age = age
        self.__passport = passport
        self.__jshshir = jshshir
    
    def get_passport(self):
        return self.__passport
    
    def resize_passport(self):
        self.__change_passport(self)
    
    def change_passport(self, new_passport):
        self.__passport = new_passport
        

p1 = Person(
    "Eshmat", 19, "AA1234567", "12345678901234"
)

p1.name = "Toshmat"
p1._Person__passport = "newpass"
# p1.__passport = "eshmatning pasporti"
# setattr(p1, "__passport", "new")

print(p1.name, p1.age, p1._Person__passport)
print(vars(p1))