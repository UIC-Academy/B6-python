"""
1) Create a list of the numbers from 5 to 500.
2) Create a list of the numbers from 0 to -100.
3) Create a list of the numbers from 100 to -100, jumping by 2.
"""

import sys

l = [i for i in range(1, 100)]

slice1 = l[2:20]
print(id(l), id(slice1))
print(sys.getsizeof(l), sys.getsizeof(slice1))
