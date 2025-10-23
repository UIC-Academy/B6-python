# Context Managers & Using the File System

### Context Managers

| Function / Concept          | Description                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------- |
| `with`                      | Enters a runtime context and ensures proper resource cleanup (e.g., closing files). |


---

### Using the File System — `os` module

| Function / Attribute     | Description                                                             |
| ------------------------ | ----------------------------------------------------------------------- |
| `os.getcwd()`            | Returns current working directory.                                      |
| `os.chdir(path)`         | Changes current working directory.                                      |
| `os.listdir(path=".")`   | Lists entries in the given directory.                                   |
| `os.curdir`              | Represents the current directory (`"."`).                               |
| `os.pardir`              | Represents the parent directory (`".."`).                               |
| `os.name`                | Returns the OS type (`'posix'`, `'nt'`, etc.).                          |
| `os.path.join(a, *p)`    | Joins one or more path components correctly for the OS.                 |
| `os.path.split(path)`    | Splits path into `(head, tail)` tuple.                                  |
| `os.path.basename(path)` | Returns the file name from the path.                                    |
| `os.path.dirname(path)`  | Returns the directory name from the path.                               |
| `os.path.exists(path)`   | Checks whether a path exists.                                           |
| `os.path.isdir(path)`    | Checks whether path is a directory.                                     |
| `os.path.isfile(path)`   | Checks whether path is a file.                                          |
| `os.remove(path)`        | Removes a file.                                                         |
| `os.mkdir(path)`         | Creates a new directory.                                                |
| `os.rmdir(path)`         | Removes an empty directory.                                             |
| `os.rename(src, dst)`    | Renames a file or directory.                                            |

---

### Using the File System — `pathlib` module

| Function / Class        | Description                                      |
| ----------------------- | ------------------------------------------------ |
| `Path()`                | Core class representing file system paths.       |
| `Path.cwd()`            | Returns current working directory.               |
| `Path.home()`           | Returns user’s home directory.                   |
| `Path.exists()`         | Returns True if path exists.                     |
| `Path.is_dir()`         | Returns True if path is a directory.             |
| `Path.is_file()`        | Returns True if path is a file.                  |
| `Path.iterdir()`        | Iterates over directory contents.                |
| `Path.mkdir()`          | Creates directory.                               |
| `Path.rename(new_name)` | Renames file or directory.                       |
| `Path.unlink()`         | Deletes a file.                                  |
| `Path.glob(pattern)`    | Yields paths matching a pattern (non-recursive). |
| `Path.rglob(pattern)`   | Recursive version of `glob()`.                   |
| `Path.read_text()`      | Reads entire file content as text.               |
| `Path.write_text(data)` | Writes text to file.                             |
| `Path.joinpath(*other)` | Joins path components.                           |
| `Path.parts`            | Returns tuple of individual path parts.          |
| `Path.parent`           | Returns parent directory as Path object.         |
| `Path.name`             | Returns final component (file name).             |
| `Path.suffix`           | Returns file extension.                          |
| `Path.stem`             | Returns file name without extension.             |


---

### 3. Examples

**Example 1: Basic Context Manager with File**

```python
with open("notes.txt", "r") as f:
    content = f.read()
print(f.closed)  # True — automatically closed
```

**Example 2: Nested Context Managers**

```python
with open("input.txt", "r") as inp, open("output.txt", "w") as out:
    for line in inp:
        out.write(line.upper())
```

**Example 3: Custom Context Manager (Manual Class)**

```python
class Resource:
    def __enter__(self):
        print("Entering context")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with Resource() as r:
    print("Inside block")
```

**Example 4: Custom Context Manager (Using `contextlib`)**

```python
from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()

with open_file("data.txt", "w") as f:
    f.write("Safe write")
```

---

**Example 5: Using `os` for Navigation**

```python
import os

print("Current:", os.getcwd())
os.chdir("..")
print("Parent:", os.getcwd())

print("Contents:", os.listdir(os.curdir))
print("OS Type:", os.name)
```

**Example 6: Using `os.path` Utilities**

```python
import os

path = "/home/user/docs/file.txt"

print(os.path.basename(path))  # file.txt
print(os.path.dirname(path))   # /home/user/docs
print(os.path.exists(path))    # True/False
print(os.path.join("/home", "user", "newdir"))  # /home/user/newdir
```

**Example 7: Directory Traversal**

```python
import os

for dirpath, dirnames, filenames in os.walk("."):
    print("Directory:", dirpath)
    print("Subdirs:", dirnames)
    print("Files:", filenames)
```

---

**Example 8: `pathlib` Basics**

```python
from pathlib import Path

p = Path(".")
print(list(p.iterdir()))       # list directory contents
print(Path.cwd())              # current directory
print(Path.home())             # home directory
```

**Example 9: Path Attributes**

```python
from pathlib import Path

f = Path("/home/user/docs/file.txt")
print(f.name)       # file.txt
print(f.stem)       # file
print(f.suffix)     # .txt
print(f.parent)     # /home/user/docs
```

**Example 10: Reading/Writing via Pathlib**

```python
from pathlib import Path

p = Path("notes.txt")
p.write_text("Context managers are safe.")
print(p.read_text())
```

**Example 11: Pattern Matching**

```python
from pathlib import Path

for file in Path(".").rglob("*.py"):
    print(file)
```

**Example 12: Directory Creation & Deletion**

```python
from pathlib import Path

p = Path("new_folder")
if not p.exists():
    p.mkdir()
    print("Created:", p)
p.rename("renamed_folder")
Path("renamed_folder").rmdir()
```
