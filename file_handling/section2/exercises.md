# Context Managers, `os`, and `pathlib` Exercises

### **Context Managers (`with`)**

1. Open a text file using `with` and print all lines.
2. Use `with` to write three lines to a file and ensure it’s closed automatically.
3. Nest two `with` blocks: read from `input.txt`, write to `output.txt`.
4. Use a `with` block to open multiple files in a single statement.
5. Simulate an exception inside a `with` block and show that the file still closes.

---

### **`os` Module Basics**

11. Print the current working directory using `os.getcwd()`.
12. Change the current working directory to a subfolder and verify with `os.getcwd()`.
13. List all files and directories in the current directory using `os.listdir()`.
14. Create a new directory named `practice_dir` with `os.mkdir()`.
15. Create a file inside `practice_dir`, then check existence using `os.path.exists()`.
16. Rename the directory `practice_dir` to `test_dir` using `os.rename()`.
17. Remove a file using `os.remove()`.
18. Remove the `test_dir` directory using `os.rmdir()`.
19. Print `os.name` and explain its meaning.
20. Use `os.path.join()` to safely construct a path to a file named `notes.txt` inside a directory `data/`.
21. Split a path using `os.path.split()` and print its head and tail.
22. Extract only the file name from a full path using `os.path.basename()`.
23. Extract only the directory name using `os.path.dirname()`.
24. Check if a path points to a directory using `os.path.isdir()`.
25. Check if a path points to a file using `os.path.isfile()`.
26. Create nested directories using `os.makedirs("a/b/c")`, then remove them.
27. Iterate through all files in the current directory and print only `.txt` files.
28. Write a script that renames all `.txt` files in a directory to `.bak` extensions.
29. Create a function that prints the absolute path of every file in a directory tree using recursion and `os.listdir()`.
30. Use `os.curdir` and `os.pardir` to navigate relative to the current working directory.

---

### **`pathlib` Module**

31. Print the current working directory using `Path.cwd()`.
32. Print your home directory using `Path.home()`.
33. Check if a file `example.txt` exists using `Path.exists()`.
34. Create a directory `temp_data` using `Path.mkdir()`.
35. Write “Hello, World!” to `temp_data/greeting.txt` using `Path.write_text()`.
36. Read the contents of that file using `Path.read_text()`.
37. Rename `greeting.txt` to `welcome.txt` using `Path.rename()`.
38. Delete `welcome.txt` using `Path.unlink()`.
39. Iterate through the current directory using `Path.iterdir()` and print names of all items.
40. Use `Path.glob("*.py")` to list all Python files in the current directory.
41. Use `Path.rglob("*.py")` to list all Python files recursively.
42. Print the `.suffix`, `.stem`, and `.name` of a file path.
43. Join two paths using `Path.joinpath()`.
44. Print the `parent` of a given path.
45. Print all parts of a path using `Path.parts`.
46. Combine `Path.is_dir()` and `Path.is_file()` to count how many files and directories exist in the current folder.
47. Write a function that deletes all `.log` files in a folder using `pathlib`.
48. Write a recursive script using `Path.rglob()` that finds all `.txt` files and prints their absolute paths.
49. Implement a backup script: copy all `.txt` files from current directory to a new directory `backup/` using `pathlib`.
50. Combine both: use a custom context manager to temporarily move into a directory (using `os.chdir()`) and list all `.py` files using `pathlib`.
