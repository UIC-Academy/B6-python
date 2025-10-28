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

14. Implement `__str__` in the `Book` class to return `"<title> by <author>"`.
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

1. **Create Student from String**
   Make a class method that creates a Student from "name,grade" string like "Anna,95"

2. **Count How Many Pets Created**
   Create a class method that tells how many Pet instances have been made

3. **Make Default Book**
   Create a class method that makes a Book with title "Unknown" and author "Unknown"

4. **Create Circle from Diameter**
   Make a class method that creates a Circle when you give it diameter instead of radius

5. **Create Birthday Person**
   Make a class method that creates a Person with age 0 (newborn)

6. **Make Random Color**
   Create a class method that makes a Color with random RGB values

7. **Create Square from Area**
   Make a class method that creates a Square when you know the area

8. **Default Settings**
   Create a class method that makes GameSettings with easy difficulty

9. **Create from List**
   Make a class method that creates a Fruit from a list like ["apple", "red"]

10. **Student from Dictionary**
    Create a class method that makes a Student from {"name": "Tom", "grade": 88}

11. **Check if Number is Even**
    Make a static method that checks if a number is even

12. **Calculate Circle Area**
    Create a static method that calculates area when given radius

13. **Check Valid Email**
    Make a static method that checks if email has "@" symbol

14. **Convert Celsius to Fahrenheit**
    Create a static method for temperature conversion

15. **Check if Triangle is Valid**
    Make a static method that checks if 3 sides can make a triangle

16. **Calculate Dog Years**
    Create a static method that converts human years to dog years (×7)

17. **Check Strong Password**
    Make a static method that checks if password has at least 8 characters

18. **Calculate Pizza Slices**
    Create a static method that calculates slices per person

19. **Check Palindrome**
    Make a static method that checks if a word reads same forwards and backwards

20. **Calculate Discount**
    Create a static method that calculates final price after discount

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
