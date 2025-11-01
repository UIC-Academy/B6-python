class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    def get_kelvin(self):
        return self.__celsius + 273
    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, temp):
        self.__celsius = temp
        
    # @celsius.getter
    # def get_temp(self):
    #     return self.__celsius
    

t1 = Temperature(41)

# print(t1.get_temp(), t1.set_temp(15))
print(t1.celsius)
t1.celsius = 12
print(t1.celsius)