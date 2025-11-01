class Account:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
    
    def __call__(self, *args, **kwds):
        print("My address is:", id(self))
        

a1 = Account("Eshmat", 111)

print(a1._name, a1.__balance)