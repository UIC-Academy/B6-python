class Phone:
    def __init__(self, name, price, color, brand):
        self.name = name
        self.price = price
        self.color = color
        self.brand = brand
    
    def call(self):
        print("Calling...")


class Domashniy(Phone):
    def __init__(self, name, price, color, brand, is_wired):
        self.is_wired = is_wired
        super().__init__(name, price, color, brand)
    
    def call(self):
        print("Tooot...Tooot...")


class SotkaOld(Phone):
    def __init__(self, name, price, color, brand, fonar):
        self.fonar = fonar
        super().__init__(name, price, color, brand)
    
    def play(self):
        print("Playing Snake Xenzia...")
        
    def message(self):
        print("Writing SMS message...")


class SotkaNew(Phone):
    def __init__(self, name, price, color, brand, is_colorful):
        self.is_colorful = is_colorful
        super().__init__(name, price, color, brand)
        
    def play(self):
        print("Playing Diamond Rush...")
    
    def message(self):
        print("Writing SMS/internet message...")
        
    def take_picture(self):
        print("Taking a picture...")
    
    def listen_music(self):
        print("Listening to music from either album or radio...")


class Smartphone(Phone):
    def __init__(self, name, price, color, brand, is_sensor):
        self.is_sensor = is_sensor
        super().__init__(name, price, color, brand)
    
    def play(self):
        print("Playing EFootball...")
    
    def surfing_social_media(self):
        print("Surfing the social media...")
        
    def take_picture(self):
        print("Taking a picture...")
    
    def listen_music(self):
        print("Listening to music from either album or radio...")
        
    def using_ai(self):
        print("Hello ChatGPT...")


class Tablet(Phone):
    def __init__(self, name, price, color, brand, size):
        self.size = size
        super().__init__(name, price, color, brand)
    
    def play(self):
        print("Playing EFootball...")
    
    def surfing_social_media(self):
        print("Surfing the social media...")
        
    def take_picture(self):
        print("Taking a picture...")
    
    def listen_music(self):
        print("Listening to music from either album or radio...")
        
    def using_ai(self):
        print("Hello ChatGPT...")
        
    def write_on_screen(self):
        print("Writing on large screen with pen...")


panasonic = Domashniy(
    name="P345",
    price=100.00,
    color="green",
    brand="Panasonic Inc.",
    is_wired=True
)
panasonic.call()

nokia3600 = SotkaOld(
    name="Nokia 3660",
    price=0,
    color="black",
    brand="Nokia",
    fonar="oq"
)
nokia3600.call()

artel = SotkaNew(
    name="Artel V5",
    price=120.00,
    color="white",
    brand="Artel",
    is_colorful=True
)
artel.listen_music()

samsung_s21 = Smartphone(
    name="Samsung S21 Ultra",
    price=120000.00,
    color="grey",
    brand="Samsung",
    is_sensor=True
)
samsung_s21.surfing_social_media()

ipad = Tablet(
    name="iPad",
    price=770000.99,
    brand="Apple",
    color="silver",
    size=15.6
)
ipad.write_on_screen()

print("DNK test result:", issubclass(Tablet, Phone))