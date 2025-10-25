# Introduction to Object-Oriented Programming (OOP)

#### 1. Related Functions, Methods, and Concepts

| Function / Concept              | Description                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------- |
| `class`                         | Blueprint for creating objects (defines data and behavior).                     |
| `object`                        | Instance of a class — concrete realization of the blueprint.                    |
| `__init__(self, ...)`           | Constructor; called automatically when an object is created.                    |
| `self`                          | Reference to the current instance (used to access instance attributes/methods). |
| `__str__(self)`                 | Returns human-readable string representation of the object.                     |
| `__repr__(self)`                | Returns unambiguous, developer-focused string representation.                   |
| `instance variables`            | Attributes unique to each object (e.g., `self.name`).                           |
| `class variables`               | Attributes shared among all instances of the class.                             |
| `instance methods`              | Functions defined inside a class that operate on instance data.                 |
| `@staticmethod`                 | Method bound to the class, not the instance (no `self`).                        |
| `@classmethod`                  | Method that receives class reference (`cls`) instead of instance.               |
| `del`                           | Deletes an object or attribute reference.                                       |
| `__del__(self)`                 | Called when an object is garbage-collected (rarely used).                       |
| `vars(obj)`                     | Returns `__dict__` of instance attributes.                                      |
| `isinstance(obj, Class)`        | Checks if object is an instance of the given class.                             |
| `hasattr(obj, name)`            | Checks if object has a given attribute.                                         |
| `getattr(obj, name[, default])` | Retrieves attribute dynamically.                                                |
| `setattr(obj, name, value)`     | Sets attribute dynamically.                                                     |
| `delattr(obj, name)`            | Deletes attribute dynamically.                                                  |

---

#### 2. Related Concepts

| Concept                           | Description                                                                                   |
| --------------------------------- | --------------------------------------------------------------------------------------------- |
| **Constructor**                   | The `__init__()` method — initializes instance state.                                         |
| **Namespace**                     | Scope that defines the accessibility of identifiers (`self` or `cls`).                        |
| **Instance vs. Class Attributes** | Instance attributes belong to each object; class attributes belong to the class itself.       |
| **Method Binding**                | Instance methods receive `self`; class methods receive `cls`; static methods receive neither. |

---

#### 3. Examples

**Example 1: Minimal Class and Object**

```python
class Person:
    pass

p = Person()
print(type(p))  # <class '__main__.Person'>
```

---

**Example 2: Class with Attributes and Methods**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old.")

p = Person("Alice", 25)
p.greet()
```

---

**Example 3: Class vs. Instance Variables**

```python
class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1  # modifies class variable
        self.id = Counter.count  # instance variable

a = Counter()
b = Counter()
print(a.id, b.id)      # 1 2
print(Counter.count)   # 2
```

---

**Example 4: Using `__str__` and `__repr__`**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(p)        # (3, 4)
print(repr(p))  # Point(x=3, y=4)
```

---

**Example 5: Classmethod and Staticmethod**

```python
class MathUtils:
    pi = 3.14159

    @classmethod
    def circle_area(cls, radius):
        return cls.pi * (radius ** 2)

    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.circle_area(5))
print(MathUtils.add(3, 4))
```

---

**Example 6: Dynamic Attribute Manipulation**

```python
class Config:
    def __init__(self):
        self.debug = True

cfg = Config()
setattr(cfg, "version", "1.0")
print(getattr(cfg, "version"))  # 1.0
print(hasattr(cfg, "debug"))    # True
delattr(cfg, "debug")
```

---

**Example 7: `vars()`, `isinstance()` Usage**

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

item = Product("Book", 15)
print(vars(item))                   # {'name': 'Book', 'price': 15}
print(isinstance(item, Product))    # True
```

---

**Example 8: Custom Destructor**

```python
class TempFile:
    def __init__(self, name):
        self.name = name
        print(f"Created {self.name}")

    def __del__(self):
        print(f"Deleted {self.name}")

t = TempFile("tmp.txt")
del t
```

---

**Example 9: Practical Object Interaction**

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

acc = Account("John", 100)
acc.deposit(50)
acc.withdraw(120)
print(acc.balance)
```

---

**Example 10: Combining All Core Ideas**

```python
class Car:
    wheels = 4  # class variable

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine_on = False

    def start(self):
        self.engine_on = True
        print(f"{self.brand} {self.model} started.")

    def stop(self):
        self.engine_on = False
        print(f"{self.brand} {self.model} stopped.")

car1 = Car("Tesla", "Model 3")
car2 = Car("BMW", "M3")
car1.start()
print(car2.wheels)
```
