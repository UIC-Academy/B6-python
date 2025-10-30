# Lecture Plan: Inheritance and Polymorphism

### 1. Related Functions, Methods, and Concepts

#### Inheritance

| Function / Concept                  | Description                                                                   |
| ----------------------------------- | ----------------------------------------------------------------------------- |
| `class Child(Parent):`              | Defines a class that inherits attributes and methods from another class.      |
| `super()`                           | Returns a temporary object of the superclass, allowing access to its methods. |
| `__init__()` in subclass            | Used to extend or override parent initialization.                             |
| `issubclass(Sub, Super)`            | Returns True if `Sub` is derived from `Super`.                                |
| `isinstance(obj, Class)`            | Returns True if object is an instance of class or subclass.                   |
| `Method Overriding`                 | Redefining a parent class method in the subclass.                             |
| `Multiple Inheritance`              | Inheriting from more than one parent class.                                   |
| `super().__init__()`                | Calls parent’s constructor from subclass.                                     |
| `__mro__` (Method Resolution Order) | Determines search order for inherited attributes/methods.                     |

#### Polymorphism

| Function / Concept       | Description                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **Polymorphism**         | Using a unified interface to operate on different data types or subclasses.                                |
| **Duck Typing**          | “If it walks like a duck and quacks like a duck, it’s a duck.” Type is based on behavior, not inheritance. |
| **Method Overriding**    | Different subclasses provide different implementations of the same method.                                 |
| **Operator Overloading** | Redefining behavior of operators (`+`, `-`, etc.) via special methods.                                     |
| `__add__(self, other)`   | Defines behavior for `+`.                                                                                  |
| `__sub__(self, other)`   | Defines behavior for `-`.                                                                                  |
| `__eq__(self, other)`    | Defines behavior for `==`.                                                                                 |
| `__lt__(self, other)`    | Defines behavior for `<`.                                                                                  |
| `__len__(self)`          | Allows usage of `len(obj)`.                                                                                |

---

### 2. Related Concepts

| Concept                             | Description                                                                                    |
| ----------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Single Inheritance**              | Child inherits from one parent.                                                                |
| **Multilevel Inheritance**          | Child inherits from a parent that is itself a child of another class.                          |
| **Multiple Inheritance**            | Child inherits from several parent classes.                                                    |
| **Overriding vs. Overloading**      | Python supports method overriding, not traditional method overloading (by signature).          |
| **MRO (Method Resolution Order)**   | Defines which parent is searched first in multiple inheritance cases.                          |
| **Abstract Base Classes (preview)** | Enforced polymorphism through abstract methods (part of `abc` module, optional at this stage). |

---

### 3. Examples

**Example 1: Basic Inheritance**

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

d = Dog()
d.speak()  # Inherited method
```

---

**Example 2: Method Overriding**

```python
class Animal:
    def speak(self):
        print("Generic sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

for a in [Dog(), Cat()]:
    a.speak()
```

---

**Example 3: Using `super()`**

```python
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

    def info(self):
        print(f"{self.name} - {self.role}")

e = Employee("Alice", "Engineer")
e.info()
```

---

**Example 4: Multiple Inheritance**

```python
class Logger:
    def log(self, msg):
        print(f"Log: {msg}")

class Saver:
    def save(self):
        print("Data saved")

class App(Logger, Saver):
    pass

a = App()
a.log("Start app")
a.save()
print(App.__mro__)
```

---

**Example 5: Multilevel Inheritance**

```python
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    def move(self):
        print("Car moving")

class ElectricCar(Car):
    def move(self):
        print("Electric car moving silently")

e = ElectricCar()
e.move()
```

---

**Example 6: `issubclass` and `isinstance`**

```python
class A: pass
class B(A): pass

b = B()
print(issubclass(B, A))   # True
print(isinstance(b, A))   # True
```

---

**Example 7: Polymorphism via Method Overriding**

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        from math import pi
        return pi * self.r ** 2

for shape in [Square(4), Circle(3)]:
    print(shape.area())
```

---

**Example 8: Duck Typing**

```python
class Dog:
    def speak(self): print("Woof")

class Cat:
    def speak(self): print("Meow")

def animal_sound(animal):
    animal.speak()

for a in [Dog(), Cat()]:
    animal_sound(a)
```

---

**Example 9: Operator Overloading**

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)
print(v1 + v2)  # Vector(3, 7)
```

---

**Example 10: Comparison and Length Overloading**

```python
class Box:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        return len(self) == len(other)

b1 = Box([1, 2, 3])
b2 = Box([4, 5, 6])
b3 = Box([1])

print(len(b1))    # 3
print(b1 == b2)   # True
print(b1 == b3)   # False
```

---

**Example 11: Unified Polymorphic Interface**

```python
class Payment:
    def pay(self):
        raise NotImplementedError

class CreditCard(Payment):
    def pay(self):
        print("Paying with credit card")

class PayPal(Payment):
    def pay(self):
        print("Paying with PayPal")

for method in [CreditCard(), PayPal()]:
    method.pay()
```

---

**Example 12: Practical Case — Employee Hierarchy**

```python
class Employee:
    def __init__(self, name):
        self.name = name
    def calc_pay(self):
        raise NotImplementedError

class HourlyEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate
    def calc_pay(self):
        return self.hours * self.rate

class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def calc_pay(self):
        return self.salary

workers = [
    HourlyEmployee("Ali", 40, 15),
    SalariedEmployee("Bob", 1200)
]

for w in workers:
    print(f"{w.name}: ${w.calc_pay()}")
```
