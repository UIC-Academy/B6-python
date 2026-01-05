# Python Iterators & Generators Exercises

## Part 1: Iterator Exercises (Beginner-Friendly)

### Basic Iterator Concepts
1. **Temperature Reader**: Create an iterator that reads daily temperatures [68, 72, 65, 70, 74] and prints each one with "°F"
2. **Book Pages**: Make an iterator for a book with 5 chapters. Print "Reading Chapter X" for each chapter
3. **Shopping Cart**: Create an iterator for a shopping cart list ["apple", "bread", "milk"] and display each item
4. **Countdown Timer**: Build an iterator that counts down from 5 to 1, then prints "Blast off!"
5. **Weekday Iterator**: Create an iterator over weekdays (Monday-Friday) and print each day

### Custom Iterator Classes
6. **Square Numbers**: Create a `Squares` class that iterates over squares of numbers from 1 to 5
7. **Alphabet Iterator**: Build an iterator that yields letters from 'A' to 'E'
8. **Even Numbers**: Create `EvenNumbers` iterator that yields first 5 even numbers
9. **Limited Counter**: Build a `Counter` iterator that stops at a specified limit (e.g., 1 to 10)
10. **Reverse Iterator**: Create an iterator that goes through a list in reverse order

### Using Built-in Iterators
11. **Sentence Words**: Use `iter()` on a sentence string, split into words, and print each word
12. **File Lines**: Read a multi-line string as if it's a file and iterate through lines
13. **Dictionary Items**: Iterate through `{"name": "Alice", "age": 30, "city": "NY"}` and print key-value pairs
14. **Zipped Lists**: Use `zip()` to combine ["Alice", "Bob"] with [85, 92] and iterate for grade report
15. **Enumerated List**: Use `enumerate()` on a todo list and print numbered tasks

### Iterator Protocols
16. **Manual Iteration**: Create a list of colors and manually use `iter()` and `next()` to print them
17. **StopIteration Handling**: Iterate manually and catch `StopIteration` to print "Done!"
18. **Reset Iterator**: Show that an exhausted iterator can't be reused (create new one)
19. **Check Iterable**: Write a function to check if an object is iterable using `iter()`
20. **Infinite Iterator**: Create a circular iterator that cycles through ["Red", "Yellow", "Green"] for traffic light simulation

### Practical Applications
21. **Batch Processor**: Create iterator that processes list of data in batches of 3
22. **Fibonacci Iterator**: Build iterator for first 7 Fibonacci numbers
23. **Prime Checker**: Iterator that yields prime numbers under 20
24. **Range-like Iterator**: Create your own simple version of `range()` for numbers 1-5
25. **Music Playlist**: Iterator that goes through song list and prints "Now playing: X"

### Combining Concepts
26. **Nested Iteration**: Iterate through list of students, each with list of grades
27. **Filter Iterator**: Use `filter()` with lambda to iterate over even numbers only
28. **Map Iterator**: Use `map()` to convert temperatures from Celsius to Fahrenheit
29. **Sorted Iterator**: Iterate through scores in sorted order without modifying original list
30. **Chained Iterators**: Chain multiple iterators to process different data sources sequentially

---

## Part 2: Generator Exercises (Beginner-Friendly)

### Basic Generators
1. **Countdown Generator**: Create generator that counts from 5 down to 1 for rocket launch
2. **Daily Sales**: Generator that yields daily sales amounts [100, 150, 200, 175]
3. **Website Visitors**: Generator yielding hourly visitor counts for a website
4. **Sensor Readings**: Simulate temperature sensor readings 5 times with random values
5. **Message Queue**: Generator that yields messages from a simulated queue

### Generator Functions
6. **Number Squares**: Generator function yielding squares of numbers 1 through 5
7. **Alphabet Generator**: Yield letters from 'A' to 'F' one by one
8. **Even Number Generator**: Generate first 6 even numbers
9. **Fibonacci Generator**: Generate first 8 Fibonacci numbers
10. **Prime Generator**: Yield prime numbers under 30

### Generator Expressions
11. **Square Roots**: Generator expression for square roots of numbers 1-10
12. **Uppercase Names**: Convert list of names to uppercase using generator expression
13. **Filter Even**: Generator expression filtering even numbers from 1-20
14. **Product Prices**: Calculate 10% discount on prices using generator expression
15. **Word Lengths**: Generator expression for lengths of words in a sentence

### Stateful Generators
16. **Running Total**: Generator that keeps yielding running total of numbers sent to it
17. **Average Calculator**: Generator that calculates running average of numbers
18. **Counter with Reset**: Generator that counts but can be reset with a sent value
19. **Toggle Switch**: Generator that toggles between "ON" and "OFF" each time it's called
20. **Accumulator**: Generator that accumulates values and yields current sum

### Practical Use Cases
21. **File Reader**: Generator that reads lines from a string (simulating file) without loading all at once
22. **Log Parser**: Generator that yields log entries matching an error pattern
23. **Pagination**: Generator that yields data in pages of 3 items each
24. **Sensor Simulator**: Infinite generator simulating temperature sensor readings
25. **Progress Tracker**: Generator that yields progress percentage from 0% to 100% in steps

### Advanced Concepts
26. **Generator Pipeline**: Chain generators: clean data → filter → transform
27. **Coroutine with `.send()`**: Generator that receives names and yields greetings
28. **Exception in Generator**: Handle `StopIteration` and generator close
29. **Infinite Sequence**: Infinite generator for natural numbers with ability to stop
30. **Batch Data Processor**: Generator that processes large dataset in chunks without memory overload

---

## Real-World Scenarios Explained

### Example for Iterators: #21 Batch Processor
```python
# Students process customer data in batches
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
batch_size = 3

class BatchProcessor:
    def __init__(self, data, batch_size):
        self.data = data
        self.batch_size = batch_size
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        batch = self.data[self.index:self.index + self.batch_size]
        self.index += self.batch_size
        return f"Processing batch: {batch}"

# Usage
processor = BatchProcessor(data, 3)
for batch in processor:
    print(batch)
# Real use: Processing large datasets without loading all into memory
```

### Example for Generators: #22 Log Parser
```python
# Students analyze server logs to find errors
def log_parser(log_lines):
    """Generator that finds error messages in logs"""
    for line in log_lines:
        if "ERROR" in line:
            yield f"Found error: {line.strip()}"

# Simulated log data
logs = [
    "INFO: System started",
    "ERROR: Disk full",
    "INFO: User login",
    "ERROR: Connection timeout",
    "INFO: Backup completed"
]

# Process logs lazily - efficient for large files
for error in log_parser(logs):
    print(error)
# Real use: Analyzing large log files without loading entire file
```
