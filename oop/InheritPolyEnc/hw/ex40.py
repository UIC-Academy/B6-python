"""
Combine isinstance() and duck typing: accept only objects that have a specific method or belong to a specific base class.
"""

class Base:
    def basemethod(self):
        raise NotImplementedError
        

class Child1(Base):
    def basemethod(self):
        print("Child has base method")
        

class IndepClass:
    def basemethod(self):
        print("Independent class also has basemethod")
        

def func(obj):
    if isinstance(obj, Base):
        obj.basemethod()
    else:
        print("Basening yoki uning bolalarining mahsuloti emas!")
    

func(Child1())
func(IndepClass())