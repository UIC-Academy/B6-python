# Inheritance and Polymorphism

### I. Inheritance

#### **Basic Inheritance**

1. Create a base class `Animal` with method `speak()`. Derive `Dog` and `Cat` classes that print different sounds.
2. Define a `Vehicle` base class with method `move()`. Inherit `Car` and `Boat`, each implementing their own `move()` message.
3. Create `Person` as a base class and `Employee` as a subclass with an additional attribute `salary`.
4. Define a parent class `Shape` with method `area()`. Inherit `Rectangle` and `Circle`, both implementing their versions of `area()`.
5. Write `class Child(Parent)` syntax to show inheritance hierarchy between `Parent`, `Child`, and `GrandChild`. Print all class names using `__class__.__name__`.
6. Demonstrate that a subclass can access attributes and methods of its parent class without redefining them.
7. Show that you can override a parent method by defining a method with the same name in a subclass.
8. Write a `superhero` example: `Hero` class with method `power()`, `Spiderman` subclass overrides `power()`.

#### **Using `super()`**

9. Create a base class `Appliance` with `__init__()` initializing `brand`. Inherit `WashingMachine` that calls `super().__init__()` and adds `capacity`.
10. Extend the `Person` → `Employee` hierarchy: call `super().__init__()` to reuse parent initialization logic.
11. Define a `Bird` class with `fly()` method and a `Parrot` subclass that calls `super().fly()` before printing an additional message.
12. Override the parent constructor but still initialize parent attributes using `super().__init__()`.
13. Demonstrate calling a parent method using `super()` when both parent and child define methods with the same name.
14. Write a subclass that modifies a parent’s attribute initialized in `__init__()` by first calling `super().__init__()`.

#### **`issubclass()` and `isinstance()`**

15. Create a class hierarchy: `Animal → Mammal → Dog`. Use `issubclass()` to verify relationships.
16. Create an instance of `Dog` and use `isinstance()` to check if it’s an instance of `Dog`, `Mammal`, and `Animal`.
17. Write a function that takes any object and prints whether it belongs to a given parent class using `isinstance()`.

#### **Method Overriding**

18. Define a parent method `describe()` in class `Employee`, override it in subclass `Manager`.
19. Write two subclasses of `Shape`: `Square` and `Circle`. Each overrides `area()` differently.
20. Create a class `Device` with a method `status()`. Override it in `Phone` and `Laptop` with specific messages.

#### **Multiple Inheritance**

21. Define classes `Flyer` and `Swimmer`, each with a `move()` method. Create `Duck(Flyer, Swimmer)` and demonstrate which `move()` runs.
22. Create `A`, `B`, and `C(A, B)` to print a message in each constructor and observe execution order.
23. Create two base classes with same method name, inherit both in a subclass, and inspect `__mro__`.
24. Combine two independent classes (`Loggable`, `Database`) into one subclass (`LoggableDatabase`) and call both parent methods.
25. Demonstrate using `super()` in multiple inheritance scenario and analyze which base class method executes first.

#### **Method Resolution Order (MRO)**

26. Create classes `A`, `B(A)`, `C(A)`, and `D(B, C)`. Print `D.__mro__`.
27. Add same method in each of the above classes and print which one is actually executed when called from `D`.
28. Build a diamond inheritance pattern and observe MRO.
29. Write a script that prints all parent classes of a class dynamically using `.__mro__`.
30. Verify that `object` is the ultimate superclass of all classes in Python.

---

### II. Polymorphism

#### **General Polymorphism**

31. Define `Dog`, `Cat`, and `Cow` each with method `sound()`. Write a loop calling `sound()` for all objects.
32. Write a function `animal_sound(animal)` that calls `animal.sound()`—test it with different subclasses.
33. Create an abstract-like parent `Shape` class with `area()` method, overridden by `Circle` and `Square`.
34. Demonstrate that the same method name `drive()` can exist in `Car` and `Bike` with different behaviors.
35. Write a list of mixed objects (`Dog`, `Car`, `Robot`) and call a method `action()` on all of them using duck typing.

#### **Duck Typing**

36. Define two unrelated classes `Duck` and `Person` each with `quack()` and `walk()`. Write a function `make_it_quack(obj)` that uses duck typing.
37. Implement a function `start(obj)` that calls `obj.run()` without checking its type—test with multiple class types that implement `run()`.
38. Show a failure example of duck typing where a required method is missing, and handle it with `hasattr()`.
39. Create two classes implementing a `connect()` method differently (`WiFi` vs `Ethernet`). Use one unified interface to test both.
40. Combine `isinstance()` and duck typing: accept only objects that have a specific method *or* belong to a specific base class.

#### **Method Overriding (Revisited)**

41. Redefine `attack()` differently in `Warrior`, `Mage`, and `Archer` classes—demonstrate polymorphism in an iteration loop.
42. Extend `Shape` with new subclasses and make each override `perimeter()`.
43. Create a `Notification` base class with subclasses `EmailNotification` and `SMSNotification`—each overrides `send()`.
44. Implement a function `notify_all(notifications)` that calls `.send()` for each element, demonstrating runtime polymorphism.

#### **Operator Overloading**

45. Create a class `Point` with `__add__` to support vector addition.
46. Extend `Point` with `__sub__` for vector subtraction.
47. Overload `__eq__` to compare two `Book` objects by title and author.
48. Overload `__lt__` to compare `Student` objects by grade.
49. Overload `__len__` in a `Team` class to return number of players.
50. Implement a `Money` class that overloads `__add__` and `__sub__` to add/subtract currency amounts.
51. Overload `__str__` and `__eq__` for a `Product` class to allow human-readable printing and equality comparison.
52. Create a `Vector` class implementing `__add__`, `__sub__`, and `__eq__` for full operator support.
53. Overload `__lt__` and `__eq__` in `Car` class to compare cars by price.
54. Write a `ShoppingCart` class that supports `len(cart)` using `__len__`.
55. Create a `BookCollection` class that supports addition of two collections using `__add__`.

#### **Advanced Polymorphism / Mixed Use**

56. Build a hierarchy `Employee → Developer` and `Manager`, each overriding `work()`. Write a loop invoking `work()` on a list of employees.
57. Create a `Shape` base class and implement a polymorphic `draw()` method in subclasses.
58. Combine inheritance and operator overloading: a `Polynomial` class that supports `+` between two polynomials.
59. Demonstrate polymorphism by defining `make_sound()` in `Dog`, `Car`, and `Alarm`. Pass all to a single function that invokes it.
60. Write a small “battle simulator”: classes `Soldier`, `Tank`, `Helicopter`, each with `attack()`. Loop over a list of mixed objects to call their respective attacks.
