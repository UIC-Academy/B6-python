from pathlib import Path

parent_excs = Path("../exercises")
parent_file = Path("../intro4.py")

print(Path.cwd())
print(Path.home())
print(Path.exists(parent_file))
print(Path.is_dir(parent_file))
print(Path.is_file(parent_excs))
print(list(Path.iterdir(parent_excs)))
print(list(Path.glob(parent_excs, "*.py")))
print(parent_excs.parts)
print(parent_excs.parent)
print(parent_file.suffix)
Path.write_text(Path("./hi.txt"), "Hello!")