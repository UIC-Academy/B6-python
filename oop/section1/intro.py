class Phone:
    name = "Phone Factory"
    year = 2020
    capacity = 14000
    
    def __init__(self, name, year, color, price):
        self.name = name
        self.year = year
        self.color = color
        self.price = price
        
    def call(self):
        print("Calling...")
    
    def play(self):
        print("Playing game...")
    
    def __str__(self):
        return f"Phone<name={self.name}>"
    
    def __add__(self, other):
        return self.price + other.price


samandars_phone = Phone(
    name="Honor X6b",
    year=2023,
    color="black",
    price=180
)

samandars_phone.call()

toxirs_phone = Phone(
    name="Samsung A10s",
    year=2022,
    color="black",
    price=150
)

toxirs_phone.play()

print(Phone.name, Phone.year, Phone.capacity)

print(toxirs_phone)
print({"one": 1})

print(samandars_phone + toxirs_phone)
print("s" + "i")


"""
class - qolip, retsept, zavod
object - qolip asosida tayyorlangan mahsulot
__init__() - zavoddan mahsulot chiqish eshigi
self - chiqish eshigidan chiqayotgan mahsulotga nisbatan pointer

"""