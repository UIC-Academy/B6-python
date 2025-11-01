class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def __lt__(self, other):
        return self.grade < other.grade

    def __gt__(self, other):
        return self.grade > other.grade
    
    def __le__(self, other):
        return self.grade <= other.grade
    
    def __ge__(self, other):
        return self.grade >= other.grade
    
    def __ne__(self, other):
        return self.grade != other.grade
    
    def __eq__(self, other):
        return self.grade == other.grade
        
    def __str__(self):
        return f"Student<{self.name}, {self.grade}>"
    

st1 = Student("Eshmat", 4.0)
st2 = Student("Toshmat", 4.1)

print(st1 < st2)
print(st1 >= st2)
print(st1 <= st2)
print(st1 != st2)

"""
> greater than (__gt__())
>= greater than or equal (__gte__())
< less than (__lt__())
<= less than or equal (__lte__())
== equal to (__eq__())
!= not equal to (__ne__())

"""