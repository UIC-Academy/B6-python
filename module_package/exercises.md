# Modules and Packages Exercises

### Modules
1. Create a module `math_utils.py` with functions `add`, `subtract`, `multiply`, and `divide`. Import and use them in `main.py`.
2. Create a module `greetings.py` with `say_hello()` and `say_goodbye()`. Import it using `import greetings as g`.
3. Create a module `converter.py` and import specific functions using `from converter import kg_to_lb, lb_to_kg`.
4. Create a module `string_ops.py` with functions manipulating strings (reverse, capitalize). Import using `from string_ops import *`.
5. Write code that checks `__name__` in a module and prints a message only if executed directly.
6. Write a module `logger.py` and access its attributes using `dir(logger)` from another file.
7. Inspect `logger.__file__` to print its absolute path at runtime.
8. Add a variable `VERSION = 1.0` in a module and import it into `main.py`. Modify and observe if it affects the original module.
9. Create a module `config.py` with constants, and import it across multiple scripts. Change one constant and observe effect in other modules.
10. Write code to list all currently loaded modules using `sys.modules`. Print if `"os"` and `"sys"` exist there.
11. Create a module with private functions (names starting with `_`) and test what happens when using `from module import *`.
12. Write a module that conditionally imports another module only if it exists, using try-except.
13. Create a module that modifies `sys.path` to import from a custom directory.
14. Write a module that uses `inspect.getsource()` to display its own source code.
15. Create a module that defines a class and import only that class using `from module import ClassName`.
16. Write a module that uses `__getattr__` to handle dynamic attribute access.
17. Create a module that implements a simple plugin system using function registration.
18. Write a module that caches expensive computations and test import behavior.
19. Create a module with circular import protection using local imports inside functions.
20. Write a module that uses `sys.modules` to prevent re-execution on multiple imports.

---

### Packages
1. Create a package `utilities/` with `__init__.py` and submodules `string_tools.py`, `math_tools.py`. Import both into `main.py`.
2. Inside `utilities/__init__.py`, import specific functions so they can be used directly after `import utilities`.
3. In a package `analytics/`, define `__all__ = ['stats', 'graphs']` inside `__init__.py`. Test what happens with `from analytics import *`.
4. Build a package `ecommerce/` with submodules `products.py`, `orders.py`, and `payments.py`. Import them using both absolute and relative imports.
5. In `ecommerce/orders.py`, import from `ecommerce/products.py` using a relative import (`from .products import Product`).
6. Modify `__init__.py` to print "Package ecommerce loaded" whenever imported.
7. Dynamically import one of the submodules in your package using `importlib.import_module`.
8. Use `dir(package)` to list available submodules and functions after import.
9. Add a global constant in `__init__.py` and access it from submodules.
10. Place a function in a submodule and re-export it in the package's `__init__.py` so it can be accessed as `package.func()`.
11. Create a namespace package without `__init__.py` files and test its behavior.
12. Build a package with subpackages (e.g., `mypackage.utils.validators`) and practice nested imports.
13. Create a package that uses `pkgutil.walk_packages()` to dynamically discover all submodules.
14. Write a package that conditionally loads submodules based on environment variables.
15. Create a package with a `setup.py` that defines entry points for console scripts.
16. Build a package that uses `importlib.resources` to access package data files.
17. Create a package with version checking in `__init__.py` to ensure compatibility.
18. Write a package that implements a plugin architecture using namespace packages.
19. Create a package with lazy loading of submodules using `__getattr__` in `__init__.py`.
20. Build a package that can be run as both a module (`python -m package`) and imported regularly.
