# Modules and Packages

### 1. Related Functions and Concepts

| Concept / Function                    | Description                                                                               |
| ------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Module**                            | A Python file (`.py`) that contains functions, classes, or variables.                     |
| **Package**                           | A directory containing multiple modules and an `__init__.py` file (treated as a package). |
| `import module_name`                  | Imports an entire module.                                                                 |
| `from module import name`             | Imports specific attributes or functions.                                                 |
| `from module import *`                | Imports all public names from a module.                                                   |
| `import module as alias`              | Imports module with a custom alias.                                                       |
| `sys.modules`                         | Dictionary of loaded modules.                                                             |
| `sys.path`                            | List of directories Python searches for modules.                                          |
| `dir(module)`                         | Lists attributes and members of the module.                                               |
| `__name__`                            | Special variable to identify module name (`"__main__"` when executed directly).           |
| `__all__`                             | Defines symbols to export when using `from module import *`.                              |
| `__init__.py`                         | Makes a directory a Python package; can be empty or initialize package imports.           |
| `__file__`                            | Path of the loaded module file.                                                           |

---

### 2. Directory and Structure Concepts

| Concept                    | Description                                                                |
| -------------------------- | -------------------------------------------------------------------------- |
| **Module Path Resolution** | Python searches modules in current directory → PYTHONPATH → site-packages. |
| **Relative Import**        | Uses dot notation inside packages (`from . import submodule`).             |
| **Absolute Import**        | Specifies full package path (`from package.submodule import func`).        |
| **Third-party Module**     | Installed via `pip`, located in `site-packages`.                           |

---

### 3. Examples

**Example 1: Simple Module**

```python
# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

```python
# main.py
import math_utils

print(math_utils.add(2, 3))
print(math_utils.multiply(4, 5))
```

---

**Example 2: Importing Specific Items**

```python
from math_utils import add, multiply

print(add(1, 2))
print(multiply(2, 3))
```

---

**Example 3: Module Alias**

```python
import math_utils as mu

print(mu.add(5, 5))
```

---

**Example 4: Using `__name__`**

```python
# demo.py
def main():
    print("Running demo module directly")

if __name__ == "__main__":
    main()
```

When executed directly:

```
$ python demo.py
Running demo module directly
```

---

**Example 5: Package Structure**

```
mypackage/
    __init__.py
    calc.py
    stats.py
```

`calc.py`

```python
def add(a, b):
    return a + b
```

`stats.py`

```python
def mean(values):
    return sum(values) / len(values)
```

`__init__.py`

```python
from .calc import add
from .stats import mean
```

Usage:

```python
import mypackage

print(mypackage.add(3, 4))
print(mypackage.mean([1, 2, 3]))
```

---

**Example 8: Relative Import Inside a Package**

```
project/
    main.py
    app/
        __init__.py
        models.py
        utils.py
```

`utils.py`

```python
def helper():
    print("Helper running")
```

`models.py`

```python
from .utils import helper

helper()
```

---

**Example 9: Inspecting Modules**

```python
import sys, math

print(sys.modules.keys())   # all loaded modules
print(math.__file__)        # module path
print(dir(math))            # attributes
```

---

**Example 10: Third-party Module**

```bash
pip install requests
```

```python
import requests

response = requests.get("https://httpbin.org/get")
print(response.status_code)
```

---

Next topic: exceptions or decorators?
