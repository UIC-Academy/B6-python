"""
Dice rolling simulation
"""

import random
import time


while True:
    first = random.randint(1, 6)
    second = random.randint(1,6)

    print(first, second)

    if first == second:
        break
    time.sleep(1)