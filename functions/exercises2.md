# Function Scopes and Nested Functions

1. **Local vs Global Print**

   ```python
   x = 10
   def show_number():
       x = 5
       print(x)
   show_number()
   print(x)
   ```

   → Predict the output, then modify it to use `global x` and observe changes.

2. **Global Counter**
   Create a global variable `count = 0`.
   Write `increment()` that increases it by 1 each time it’s called.

3. **Shadowing Practice**
   Define a variable `name = "outer"`.
   Inside a function, redefine `name = "inner"`.
   Print both and note the difference.

4. **Temperature Tracker**
   Use `global` to keep a running total of `temperatures` list across multiple function calls.

5. **Nonlocal Demo**

   ```python
   def outer():
       x = "outer"
       def inner():
           nonlocal x
           x = "changed"
           print("Inner:", x)
       inner()
       print("Outer:", x)
   outer()
   ```

   → Explain what happens and why.

6. **Scope Confusion**
   Try to print a variable defined inside a function, outside the function.
   Observe the `NameError`. Explain why it occurs.

7. **Resetting Globals**
   Create two functions: `set_value()` and `reset_value()`.
   Both modify a global variable differently. Demonstrate the changes.

8. **Counter with Local State**
   Create a function `counter()` that defines `count = 0` inside it and increments `count` each time it’s called **inside the same execution**.
   Then see what happens if you call `counter()` multiple times.

9. **Local Calculation**
   Write a function `sum_and_print(a, b)` that defines a local variable `total`, prints it, and verify it’s not accessible outside.

10. **Outer Variable Reuse**

    ```python
    x = 100
    def test():
        print(x)
    test()
    ```

    Then define another `x` inside the function. Observe shadowing.

---

11. **Basic Nesting**
    Define a function `outer()` that prints “Outer start”, defines an inner function `inner()` printing “Inner call”, and then calls it.

12. **Sum Helper**
    Create a function `calculate(a, b)` that defines an inner function `add()` to return the sum, and then prints it.

13. **Greeting Generator**
    Outer function `greet(name)` defines inner `message()` that returns `"Hello, <name>!"`.
    Outer returns the result of `message()`.

14. **Double Inner Calls**
    Have two nested inner functions, `inner1()` and `inner2()`.
    Each prints something. Call them both inside outer.

15. **Inner Returns Inner**
    Have `outer()` return `inner()` without parentheses first (returning the function itself), then with parentheses (returning its result). Compare the difference.

16. **Mathematical Nesting**
    Outer function `math_ops(x, y)` defines `add()`, `sub()`, and `mul()` inside.
    Each prints a result. Call all three.

17. **Nested Multiplication Table**
    `table(n)` defines inner `show_row(i)` that prints one row.
    Loop inside `outer()` to call inner for each `i`.

18. **Inner Capturing Outer Variable**

    ```python
    def outer():
        message = "Hello"
        def inner():
            print(message)
        inner()
    outer()
    ```

    Try changing `message` inside `inner()` and see what happens with and without `nonlocal`.

19. **Sum List Inside Function**
    `process_list(nums)` defines `compute_sum()` inside and calls it.
    Return both the list length and sum.

20. **Outer Returning Multiple Functions**
    Define `outer()` that returns two inner functions `add_one()` and `add_two()`.
    Store them in variables and call separately.


## ⚙️ Theme 3: Functions as First-Class Objects — 10 Exercises

21. **Return a Function**
    Write a function `make_printer(msg)` that returns another function which prints `msg` when called.
    Test it with different messages.

22. **Pass Function as Argument**
    Write `apply_twice(func, value)` which applies `func` to `value` twice.
    Example: `apply_twice(lambda x: x+1, 5)` → 7.

23. **Function List**
    Store three simple functions (`add`, `sub`, `mul`) in a list and loop through calling each on `(2, 3)`.

24. **Function in Dict**
    Create a dictionary mapping operation names to functions:

    ```python
    ops = {
        "add": lambda a,b: a+b,
        "mul": lambda a,b: a*b
    }
    ```

    Then call them by key.

25. **Chooser Function**
    Define `choose_func(option)` that returns a specific function based on the `option` argument ("upper", "lower", etc.), then use it on a string.

26. **Delayed Execution**
    Define a function `delayed(func)` that prints “waiting…” and then calls the function passed in.

27. **Greeting Factory**
    `greeting_factory(lang)` returns a function that greets in that language.
    Example: `en_greet = greeting_factory("en")`; `en_greet("Ali")` → “Hello, Ali”.

28. **Higher-Order Math**
    `operate_on_list(nums, func)` applies the given function to all numbers and returns a new list.
    Try `lambda x: x**2` and `lambda x: x+10`.

29. **Function Pipeline**
    Create a function `compose(f, g)` that returns a new function applying `f(g(x))`.
    Test with `f=lambda x:x+2` and `g=lambda x:x*3`.

30. **Dynamic Selector**
    Write `get_transformer(choice)` which returns a transformation function:

    * `"reverse"` → reverses a string
    * `"capitalize"` → capitalizes
    * `"words"` → splits into words
      Use it dynamically in a loop.
