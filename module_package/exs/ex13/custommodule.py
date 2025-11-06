import sys
from pathlib import Path

basepath = Path.cwd()
loggerpath = Path.cwd() / Path("exs") / Path("ex6")

sys.path.append(loggerpath.__str__())
sys.path.append(basepath.__str__())

print(sys.path)

import logger
import intro


print(dir(logger))
print(dir(intro))