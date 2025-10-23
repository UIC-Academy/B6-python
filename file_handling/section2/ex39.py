from pathlib import Path


for path in Path.iterdir(Path("../files")):
    print(path)