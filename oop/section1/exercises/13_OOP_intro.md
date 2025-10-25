# OOP Intro Exercises

### **Class and Object Basics**

1. Define a `Car` class with attributes `brand` and `model`. Create two objects and print their attributes.
2. Create a `Person` class with `name` and `age` attributes. Instantiate it and print formatted output using f-strings.
3. Define a `Book` class and create three different `Book` objects representing different titles.
4. Create a `Dog` class with a method `bark()` that prints “Woof!”. Call it from an object.
5. Define a `Student` class where `__init__` prints “New student created.” when a new object is created.
6. Add a method `introduce()` to `Person` that prints “Hi, I am <name>.” and test it.
7. Write a class `Rectangle` that calculates and prints its area and perimeter using instance methods.
8. Create a `Circle` class with a radius attribute and a method `area()` that returns the circle’s area.

---

### **`__init__`, `self`, and Instance Variables**

9. Define a `Laptop` class with instance variables `brand`, `ram`, and `price`. Create two laptops and print details.
10. Create a `Movie` class where `__init__` takes `title`, `year`, and `genre`. Add a method `info()` to return a formatted string.
11. Write a `BankAccount` class with methods `deposit()` and `withdraw()` modifying an instance variable `balance`.
12. Create a `Player` class that tracks `name` and `score`. Write a method `add_score(points)` to increase the score.
13. Define a `Point` class representing x, y coordinates. Add a method `distance_from_origin()` returning Euclidean distance.

---

### **`__str__` and `__repr__`**

14. Implement `__str__` in the `Book` class to return “<title> by <author>”.
15. Implement both `__str__` and `__repr__` for the `Person` class. Compare printed outputs from `print(person)` and `repr(person)`.
16. In the `Rectangle` class, implement `__repr__` to return “Rectangle(width=..., height=...)”.
17. Add a `__str__` to `BankAccount` showing account owner and current balance.

---

### **Class Variables**

18. Define a `Student` class with a class variable `school = "Greenwood High"`.
19. Create multiple `Student` objects and show that all share the same `school` variable.
20. Change `Student.school` to `"Bluebell Academy"` and show how all instances reflect the change.
21. Add a class variable `count` to `Car` that keeps track of how many cars have been created.
22. Increment `count` in the constructor and print it after creating several objects.

---

### **Static and Class Methods**

23. Add a `@staticmethod` to `MathUtils` class that returns the square of a number.
24. Add a `@classmethod` in `Person` that creates a `Person` object from a formatted string like `"John-25"`.
25. Add a `@classmethod` `from_birth_year(cls, name, year)` that calculates age and returns a new `Person`.
26. Create a `@staticmethod` in `Temperature` class that converts Celsius to Fahrenheit.
27. Add a `@classmethod` to `Circle` that creates a circle given its diameter instead of radius.

---

### **`del`, `__del__`, and Attribute Operations**

28. Create a `TempFile` class whose `__del__` prints “File deleted” when object is garbage collected.
29. Create an object, delete it with `del`, and observe the destructor message.
30. Add a `delete_account()` method to `BankAccount` that deletes the `balance` attribute using `del self.balance`.
31. Use `vars()` to print all attributes of a `Car` object as a dictionary.
32. Use `hasattr()` to check if a `Person` object has the attribute `age`.
33. Use `getattr()` to safely retrieve `height` from a `Person` object with default `"Unknown"`.
34. Use `setattr()` to dynamically add a new attribute `nationality = "Uzbek"` to a `Person` instance.
35. Use `delattr()` to remove an attribute from an existing object and verify using `hasattr()`.

---

### **Type Checking and Introspection**

36. Create two classes, `Cat` and `Dog`, and use `isinstance()` to check if an object is a `Dog`.
37. Create a function `describe(obj)` that prints the class name of any object passed in using `obj.__class__.__name__`.
38. Use `issubclass()` to verify relationships between `Animal`, `Dog`, and `Poodle` classes.
39. Print the `__dict__` of an object to inspect its stored instance variables.
40. Combine everything: write a `Vehicle` class with class variable `vehicle_count`, instance variables `make` and `year`, a static method `is_motorized()`, a class method `from_string()`, and a custom `__str__`—demonstrate all functionality.
