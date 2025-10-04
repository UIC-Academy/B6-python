# 50 Python Function Exercises

## 🧩 **Section 1: Function Basics (1–10)**

Focus: defining and calling functions, difference between `print` and `return`.

1. **Simple Greeting:**
   Write a function `greet()` that prints `"Hello, world!"` when called.

2. **Return vs Print:**
   Write two functions: one prints the sum of two numbers, the other returns the sum.
   Show the difference when you use them in another expression.

3. **Personal Greeting:**
   Define a function `greet_user(name)` that returns `"Hello, <name>!"`.

4. **Odd or Even:**
   Create a function `is_even(n)` that returns `True` if a number is even, else `False`.

5. **Square Function:**
   Write a function `square(x)` that returns the square of the number.
   Print the result of squaring numbers from 1 to 5 using a loop.

6. **Maximum of Two:**
   Write a function `max_of_two(a, b)` that returns the larger of two numbers using an `if` statement.

7. **Multiple Calls:**
   Define a function `repeat_message(msg, n)` that prints the message `n` times using a loop.

8. **String Length:**
   Write a function `string_length(s)` that returns the length of a string.
   Use it in a loop to print lengths of each word in a list.

9. **Sum of List:**
   Define a function `sum_list(numbers)` that returns the sum of all numbers in a list.

10. **Greeting All:**
    Write a function `greet_all(names)` that takes a list of names and prints a greeting for each.

---

## ⚙️ **Section 2: Parameters, Arguments, and Logic (11–20)**

Focus: positional and keyword parameters, conditional logic, returning values.

11. **Minimum of Three:**
    Write a function `min_of_three(a, b, c)` that returns the smallest number.

12. **Check Membership:**
    Write a function `contains(item, collection)` that returns `True` if `item` is found in the list, set, or tuple.

13. **Count Vowels:**
    Write a function `count_vowels(word)` that returns the number of vowels in the given word.

14. **Word Reverser:**
    Write a function `reverse_word(word)` that returns the reversed version of the string.

15. **Grade Calculator:**
    Define a function `get_grade(score)` that returns `"A"`, `"B"`, `"C"`, etc., based on numeric score using if-elif-else.

16. **Power Function:**
    Write a function `power(base, exp=2)` that returns `base ** exp`.
    Demonstrate both default and explicit argument usage.

17. **Temperature Converter:**
    Create a function `to_celsius(fahrenheit)` and `to_fahrenheit(celsius)` using appropriate formulas.

18. **Unique Elements:**
    Write a function `unique_elements(lst)` that returns a set of unique values from a list.

19. **Factorial Calculation:**
    Define a function `factorial(n)` that returns the factorial of a positive integer using a loop.

20. **Filter Positives:**
    Write a function `filter_positive(nums)` that returns a list of only positive numbers.

---

## 🧠 **Section 3: Advanced Parameters – *args, **kwargs (21–30)**

Focus: flexible argument handling and positional vs keyword arguments.

21. **Sum of All:**
    Define `sum_all(*args)` that returns the sum of all arguments passed.

22. **Multiply All:**
    Write a function `multiply_all(*args)` that multiplies all numbers passed.

23. **Student Info:**
    Define a function `student_info(name, age, **details)` that prints student information.
    Example call:

    ```python
    student_info("Ali", 21, grade="A", country="Uzbekistan")
    ```

24. **Keyword Override:**
    Write a function `describe_pet(animal, name="Unknown")`.
    Call it using both positional and keyword arguments.

25. **Flexible Average:**
    Define a function `average(*numbers)` that returns the average of any count of numbers.

26. **Dictionary Printer:**
    Write a function `print_dict(**kwargs)` that prints key-value pairs.

27. **Args & Kwargs Combo:**
    Create a function `show_data(*args, **kwargs)` that prints args and kwargs separately.

28. **Sum or Multiply:**
    Write a function `calculate(*args, operation="sum")` that performs either sum or multiplication depending on the keyword argument.

29. **Configurable Greeting:**
    Define a function `custom_greet(name, **options)` that can change greeting style:

    ```python
    custom_greet("Ali", prefix="Dear", suffix="!")
    ```

30. **Build Sentence:**
    Write a function `build_sentence(*words, sep=" ")` that joins words with the given separator and returns the sentence.

---

## 🧮 **Section 4: Functions + Collections (31–40)**

Focus: interaction with lists, dicts, sets, and tuples.

31. **List Squarer:**
    Write `square_all(nums)` that returns a new list containing the squares of all numbers.

32. **Dict Inverter:**
    Define `invert_dict(d)` that returns a new dict where keys and values are swapped.

33. **Set Intersection:**
    Write a function `common_elements(set1, set2)` that returns their intersection.

34. **Tuple Converter:**
    Define a function `list_to_tuple(lst)` that converts a list into a tuple.

35. **Dict Search:**
    Write `find_key(d, value)` that returns the key matching the given value in a dictionary.

36. **List Filter Function:**
    Define `filter_even(numbers)` that returns a list of even numbers only.

37. **Longest String:**
    Write a function `longest_word(words)` that returns the word with the maximum length.

38. **Merge Dictionaries:**
    Define a function `merge_dicts(d1, d2)` that combines both into one dictionary.

39. **Unique Count:**
    Write `unique_count(lst)` that returns how many unique elements are in the list.

40. **List to Set Converter:**
    Define `list_to_set(lst)` that removes duplicates and returns a set.

---

## 🔁 **Section 5: Intermediate Applications (41–50)**

Focus: logic combination, nested loops, function composition, practical tasks.

41. **Prime Checker:**
    Write a function `is_prime(n)` that returns `True` if `n` is a prime number.

42. **Palindrome Checker:**
    Define `is_palindrome(s)` that returns `True` if the string reads the same backward.

43. **Word Frequency:**
    Write a function `word_count(sentence)` that returns a dictionary with word frequencies.

44. **Character Counter:**
    Define `char_frequency(s)` that returns how many times each character appears in a string.

45. **Sort by Length:**
    Write a function `sort_by_length(words)` that returns a list sorted by word length.

46. **Find Max Value in Dict:**
    Define `max_value(d)` that returns the key with the highest value.

47. **Email Validator (Simple):**
    Write `is_valid_email(email)` that checks if an email contains `'@'` and `'.'`.

48. **Nested Function:**
    Define `outer_function(x)` that contains an `inner_function(y)` returning `x + y`.
    Return the result of calling `inner_function`.

49. **Custom Filter:**
    Write a function `custom_filter(numbers, condition)` where `condition` is another function (e.g., `is_even`).
    Return numbers that satisfy the condition.

50. **Student Grades Average:**
    Write a function `average_grades(grades_dict)` that takes a dictionary like:

    ```python
    {"Ali": [90, 80, 85], "Sami": [70, 75, 72]}
    ```

    and returns a new dict with each student’s average score.

---

Would you like me to generate **the answer keys (solutions)** for these exercises next — perhaps grouped by section, with explanations on `return` vs `print` and argument usage?
