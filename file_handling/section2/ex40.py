from pathlib import Path
import os


curdir = Path(Path.cwd())

print(list(file.name for file in curdir.glob("*.py")))

fdir = curdir.parent
print(fdir)

print(list(file.name for file in fdir.glob("*.py")))
print(list(file.name for file in fdir.rglob("*.py")))

res = curdir.joinpath("templates", "html")

print(res, res.exists())