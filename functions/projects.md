# 20 Creative Function-Based Exercises (Mixed Topics)

### 1. **Smart Grade Evaluator**

Write a function `evaluate_students(data: dict[str, list[int]]) -> dict[str, str]`
Each student has a list of scores.

* Compute average using an inner helper function.
* Return a dict mapping student → grade ("A", "B", "C"...).
* Use default grading thresholds as optional keyword args (`kwargs`).

---

### 2. **Custom Joiner**

Implement `smart_join(strings: list[str], sep: str = "-", *, upper: bool = False) -> str`

* If `upper=True`, return joined string in uppercase.
* Use lambdas for conditional transformations.

---

### 3. **Scoped Counter**

Make a function `counter(start=0)` that returns an **inner function** `increment()` which increases the count.
Demonstrate that the counter maintains state using `nonlocal`.

---

### 4. **Keyword-Based Shopping Cart**

`checkout(*items, tax=0.1, discount=0.0)`
Each `item` is a tuple `(name, price)`.
Compute total price applying tax and discount.
Use formatted string output and return summary dict.

---

### 5. **Lambda Sorting Challenge**

Given a list of tuples `[(“apple”, 3), (“banana”, 1), (“cherry”, 2)]`,
Write a function `sort_items(items, key_func=lambda x: x[1])`
that sorts by key_func (default: second element).
Allow user to override key_func with a lambda for name length, etc.

---

### 6. **Word Frequency Analyzer**

`word_count(text: str) -> dict[str, int]`
Use:

* `split()` and loops to count words.
* `defaultdict` or `.get()`.
* A lambda to sort by frequency.
  Then extend it to take an optional stopword list via `kwargs`.

---

### 7. **Scoped Configuration Loader**

Create a function `load_config()` that defines inner function `read_env(var)` using a local dictionary as a “mock environment”.

* Demonstrate local and global scopes (define a global `ENV_PATH`).
* Return combined config as dict.

---

### 8. **Student Ranking Project**

`rank_students(students: list[dict], *, key="average")`

* Each student dict has name and marks list.
* Compute average using an inner helper.
* Use a lambda to sort students.
* Return the top 3.

---

### 9. **Dynamic Argument Analyzer**

Write a function `inspect_args(*args, **kwargs)`

* Print the type and value of each arg.
* Return summary dict.
  Useful for debugging.

---

### 10. **Vowel Extractor**

`extract_vowels(text: str, *, unique=False) -> list[str]`

* Use `set` to remove duplicates if `unique=True`.
* Use default arguments for vowels list.
* Return vowels in original order using list comprehension inside the function.

---

### 11. **Lambda Dictionary Transformer**

Given a dict of student → score,
write `transform_scores(scores, transform=lambda x: x)`
that applies the lambda to all values.
Example:
`transform_scores(scores, lambda x: x + 10 if x < 50 else x)`

---

### 12. **Playlist Builder**

`make_playlist(*songs, shuffle=False, repeat=1)`

* Use `random.shuffle` if `shuffle=True`.
* Return a list with repeated playlist.
* Print total duration with f-string.
* Showcase scope and mutable default pitfalls (avoid default `[]`).

---

### 13. **Local Currency Formatter**

`format_currency(amount: float, *, symbol="$", precision=2)`

* Use a lambda to round and format.
* Include function annotations and docstring.

---

### 14. **Mini Menu System**

Create a `menu()` function that defines **inner functions** like `add_item()`, `remove_item()`, etc.
Store data in a local list and return the inner functions as a dict of callable menu actions.
Test the closures.

---

### 15. **Recursive Lambda Countdown**

Implement `countdown = lambda n: 1 if n <= 1 else n * countdown(n-1)`
Then wrap it in a function that validates input and prints each step using a `while` loop.

---

### 16. **Filter Factory**

`make_filter(condition_func)` returns a function that filters a list according to condition_func.
Example:

```python
even_filter = make_filter(lambda x: x % 2 == 0)
print(even_filter([1, 2, 3, 4]))
```

Demonstrate scope and closures.

---

### 17. **Contact Book Project**

`add_contact(name, phone, contacts=None)`

* Use default argument `contacts=None` to avoid mutable defaults.
* Return updated list.
  Add another function `search_contact(contacts, keyword)` to search case-insensitively.

---

### 18. **Stats Aggregator**

`calculate_stats(numbers: list[int], *, ops=None)`

* ops is a dict like `{ "sum": sum, "max": max, "min": min }`.
* Compute all results dynamically.
  If no ops provided, use a default dict of lambdas.

---

### 19. **Dynamic Message Builder**

`build_message(template: str, **kwargs)`

* Replace `{name}`, `{age}`, etc. using `template.format(**kwargs)`.
* Use default arguments for fallback values.
* Demonstrate **string formatting + kwargs unpacking**.

---

### 20. **Quiz Game (Mini Project)**

Build a simple quiz app:

* Questions in a list of dicts.
* `ask_question(question: dict)` → returns True/False.
* `run_quiz(questions)` → loops through and counts score.
* Use nested function for scoring logic.
* Include lambdas for correctness checks.
* Use function annotations for clarity.
