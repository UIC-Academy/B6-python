import logger
import math
import requests

# print(dir(logger))
# print(logger.__file__)
print(math.__file__)
print(requests.__file__)


from logger import VERSION

VERSION = "1.0.1"

print(VERSION)
print(dir(logger))