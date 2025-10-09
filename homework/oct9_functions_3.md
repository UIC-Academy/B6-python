# Functions as First-Class Objects (with Lambdas)

### Level 1: Functions as Values (Warm-up)

1. Write a function `greet()` that prints `"Hello"`. Assign it to another variable and call it using that variable.
2. Store two functions (`add()`, `subtract()`) inside a list and call them in a loop with arguments.
3. Store three different arithmetic functions in a dictionary with keys `"add"`, `"sub"`, `"mul"`. Call them using user input.
4. Create a list of lambdas that each multiply a number by `1, 2, 3, 4, 5`. Call each lambda with the number `10`.
5. Write a function `apply(func, value)` that applies a given function to a value. Test with both a regular function and a lambda.
6. Write a function that takes another function and two numbers and returns the result of applying that function to both.
7. Define a list of numbers. Define a lambda that squares a number. Use a for-loop to print the result of applying the lambda to each number.
8. Store three lambdas performing different string operations (uppercase, lowercase, title). Apply each to `"python"`.
9. Create a tuple of functions that add `5`, `10`, and `15` to a number. Use a for-loop to apply all to the number `20`.
10. Define a function `choose(condition)` that returns one of two lambdas — one that adds 10 if `condition` is True, else subtracts 10. Test both cases.

---

### Level 2: Passing and Returning Functions

11. Write `operate(a, b, op)` where `op` is a function (like add, sub, etc.). Pass lambdas directly as `op`.
12. Write a function `make_multiplier(n)` that returns a lambda which multiplies its argument by `n`. Test with 2, 3, 5.
13. Write a function `select_function(name)` that returns a lambda for `"square"`, `"cube"`, or `"double"`.
14. Create a function `filter_even(func, numbers)` that filters numbers based on a condition given by `func`.
15. Write a function that returns different lambdas depending on whether a string starts with a vowel or not.
16. Define a list of names. Write a function that takes a function `transformer` and applies it to every name in the list.
17. Write a function `conditional_apply(numbers, func_true, func_false)` that applies `func_true` if number is even, else `func_false`.
18. Write a function that takes another function and prints its name and result (use `func.__name__` and `func()` call).
19. Make a higher-order function `repeater(func, n)` that returns a new function calling `func` `n` times.
20. Create a `choose_operator(symbol)` that returns a lambda performing that arithmetic operation (`+`, `-`, `*`, `/`).

---

### Level 3: Lambda Practice with Lists, Tuples, Dicts

21. Sort a list of strings by their length using a lambda as `key`.
22. Given a list of tuples `(name, age)`, sort by age using a lambda.
23. Use a lambda to extract all first elements of a list of tuples.
24. Map a lambda that reverses strings over a list of words.
25. Use a lambda inside `filter()` to extract numbers divisible by 3 or 5 from a list.
26. Given a dictionary of products and prices, use a lambda to print only those above a certain price.
27. Convert a list of strings to uppercase using a lambda and `map()`.
28. Given a list of numbers, use a lambda inside `map()` to replace negative numbers with `0`.
29. Sort a list of tuples `(city, population)` by population in descending order using a lambda.
30. Write a function `apply_all(funcs, value)` that applies all functions in a list to the value and returns a list of results.

---

### Level 4: Conditionals + Loops + Lambdas

31. Write a lambda that returns `"Even"` if a number is even, else `"Odd"`.
32. Use a list comprehension with a lambda inside to convert a list of numbers into `"Even"`/`"Odd"` labels.
33. Define a list of strings. Use a lambda and `filter()` to extract those starting with a vowel.
34. Create a function that accepts a list of numbers and a lambda `condition`. It prints numbers satisfying the condition.
35. Write a function that counts how many elements in a list satisfy a condition (passed as lambda).
36. Use lambdas to generate a list of factorials for numbers 1–5 (hint: use `for` loop and reduce-like logic).
37. Use a lambda to decide whether a string is a palindrome (ignore case).
38. Create a `switch_case` lambda that converts a string to lowercase if it’s uppercase, and vice versa.
39. Given a list of integers, use a lambda inside a for-loop to print `"Fizz"` if divisible by 3, `"Buzz"` if divisible by 5, `"FizzBuzz"` if both.
40. Write a lambda that checks if a number is prime (basic implementation with loop).

---

### Level 5: Nested + Returned Lambdas (Higher-order Thinking)

41. Write `make_power(n)` that returns a lambda to raise numbers to power `n`.
42. Write a function that takes a list of functions and applies them one after another to a value (function composition).
43. Write a function `chain(func1, func2)` that returns a new function applying both in sequence.
44. Write `make_counter()` that returns a lambda remembering how many times it was called (use closure).
45. Create a function `string_repeater(s)` returning a lambda that repeats `s` a given number of times.
46. Write a function `choose_lambda(flag)` that returns a lambda doing addition if flag=True, else subtraction.
47. Build a list of lambdas that return the square of 0 to 4 — fix the late-binding issue properly.
48. Write a function that takes a function `f` and returns a new function that adds `1` to its result.
49. Write a lambda that accepts another lambda and applies it twice to a number.
50. Build a simple calculator using a dictionary of lambdas for `+`, `-`, `*`, `/`, and let user choose operation.
