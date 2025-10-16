# Exception Handling Exercises

1. Write a program that divides two numbers input by the user and handles `ZeroDivisionError` and `ValueError`.
2. Create a function that takes a list of integers and returns their inverses, skipping zeros using exception handling.
3. Write code that opens a file and reads its contents safely using `try-except-finally`, ensuring the file is always closed.
4. Build a program that converts a list of strings to integers; handle non-numeric strings using exception handling.
5. Create a loop that reads user input until they provide a valid integer. Use exceptions to handle invalid inputs.
6. Write a function that tries to access a key in a dictionary and catches `KeyError` if it doesn’t exist.
7. Implement a decorator that catches any exception raised inside the decorated function and prints an error message.
8. Write a program that catches `IndexError` when accessing an element in a list out of range.
9. Define a function that takes two lists and divides corresponding elements, handling mismatched lengths and division errors.
10. Create a custom exception `EmptyListError` and raise it when a function receives an empty list.
11. Write a function that checks if a string contains only digits. If not, raise a `ValueError`.
12. Implement a function that raises a custom `NegativeNumberError` if the input is a negative integer.
13. Create a program that parses a tuple of numbers and skips invalid entries using `try-except`.
14. Write a program that safely converts user input to a float using exception handling and retries until valid input.
15. Build a function that loads configuration data from a dictionary. Raise a `KeyError` if a required field is missing.
16. Write a function that takes a list of filenames, opens each file, and handles `FileNotFoundError` gracefully.
17. Implement nested `try-except` blocks: first to open a file, then to parse its contents as integers.
18. Create a program that demonstrates the use of `else` and `finally` blocks in a `try-except` construct.
19. Write a function that accepts a string, converts it to an integer, and doubles it. Handle exceptions for invalid types.
20. Build a decorator that retries a function three times if it raises an exception before giving up.
21. Create a function that extracts items from a dictionary, raises a `TypeError` if the argument is not a dictionary.
22. Implement a custom `OutOfRangeError` for a function that validates numeric input within a specified range.
23. Write a function that accepts a list and raises a `TypeError` if any element is not a number.
24. Build a script that iterates through a list of values, converts them to integers, and logs any conversion errors.
25. Write code that tries to split a string by spaces and convert each word to an integer, handling `ValueError`.
26. Create a function that attempts to access a specific index in a list and uses a default value if out of range.
27. Implement a custom exception `InvalidEmailError` raised when a string doesn’t contain “@”.
28. Build a function that downloads data (simulate with random success/failure) and retries on failure using `try-except`.
29. Write a lambda function wrapped inside `try-except` that divides two numbers.
30. Create a higher-order function that takes another function and executes it with safe exception handling.
31. Implement a decorator that logs the exception type and message for any error in the wrapped function.
32. Write a program that reads integers from a file and sums them, skipping non-numeric lines.
33. Create a function that validates a password and raises different custom exceptions (`TooShortError`, `NoDigitError`, etc.).
34. Write a script that iterates over a list of tuples `(a, b)` and divides them safely, ignoring invalid pairs.
35. Implement a program that uses `try-except` in a `for` loop to process multiple items and continues after errors.
36. Write a function that removes duplicates from a list but raises an exception if the input isn’t iterable.
37. Build a custom `InvalidOperationError` and raise it when a function receives an unsupported operation string.
38. Implement a context manager using `try-except-finally` to simulate file opening and closing manually.
39. Create a script that reads JSON data and catches `json.JSONDecodeError` for invalid JSON strings.
40. Combine decorators and exceptions: create a decorator that measures execution time and catches exceptions during execution.
