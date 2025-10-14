# Decorators - Exercises

### Main Usages of Decorators

1. Write a decorator that prints `"Starting..."` before and `"Done."` after a function runs.
2. Create a decorator that measures how many times a function was called and prints the count each time.
3. Write a decorator that prints the name of the function being called.
4. Write a decorator that converts a function’s string return value to uppercase.
5. Write a decorator that checks if a string argument is empty before calling the function.
6. Write a decorator that prevents execution if a number argument is negative.
7. Create a decorator that prints `"Executing <function name>"` and the arguments it was called with.
8. Make a decorator that prints the type of each argument passed to the function.
9. Write a decorator that repeats the function’s output 3 times.
10. Write a decorator that replaces `None` return values with `"No result"`.
11. Create a decorator that only allows even numbers to be passed to the function.
12. Write a decorator that filters out duplicate elements from a list argument before calling the function.
13. Write a decorator that converts all string arguments to lowercase before calling the function.
14. Write a decorator that sorts any list or tuple argument before passing it to the function.
15. Create a decorator that checks if all numeric arguments are positive; if not, print a warning and skip execution.
16. Write a decorator that limits how many times a function can be called (e.g., max 5 times).
17. Create a decorator that counts how many elements in a list argument satisfy a certain condition (e.g., even numbers).
18. Write a decorator that skips calling the function if the first argument is an empty list or string.
19. Write a decorator that removes `None` values from list arguments before calling the function.
20. Write a decorator that reverses all string arguments passed to the function.
21. Create a decorator that multiplies a numeric return value by 10.
22. Write a decorator that wraps a function’s string result in parentheses.
23. Write a decorator that converts a function’s return type:

* if list → tuple
* if tuple → list

24. Create a decorator that joins the characters of a string return value with `-`.
25. Write a decorator that returns a sorted version of any iterable returned by the function.
26. Write a decorator that applies a given lambda to every element of a list returned by the function.
27. Write a decorator that adds `"Hello, "` before and `"!"` after a string return value.
28. Write a decorator that doubles each element in a list returned by the function.
29. Write a decorator that converts a dictionary’s values to uppercase if they are strings.
30. Create a decorator that, when the function returns a list of numbers, filters out the odd ones.


---

### Challenging Exercises

1. **Implement a simple LRU (Least Recently Used) cache decorator**

   * Limit stored results to *n* recent function calls (use a list or dict to manage keys and eviction).
   * When cache is full, remove the oldest used entry.
   * Must work with functions taking simple arguments like integers or strings.

2. **Implement a retry-on-failure decorator**

   * Retry calling the function up to *n* times if it raises an exception (use `try-except` and a loop).
   * After all retries fail, print `"Function failed after n attempts."`.
   * Example use: simulate unreliable computations (like division by random numbers).

3. **Write a time-based caching decorator**

   * Cache results for each argument for a fixed duration (say 5 seconds).
   * After expiration, the function recomputes and updates the cache.
   * Use timestamps (from `time.time()`), but no external libraries.

4. **Implement a call-logger decorator with history tracking**

   * Keep a list (closure-based) that stores each function call’s arguments and return value.
   * Provide an inner function `get_history()` accessible from the wrapped function (e.g., `func.history()`) to inspect call history.

5. **Implement a “conditional execution” decorator**

   * Accept a condition function (lambda or callable) as an argument to the decorator.
   * Only execute the wrapped function if the condition returns `True` for the given arguments; otherwise, print `"Skipped due to condition."`.
   * For example: `@conditional(lambda x: x > 0)` should skip function calls with negative inputs.
