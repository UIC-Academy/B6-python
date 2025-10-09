"""
Check Membership
"""
from typing import Iterable

def contains(item: any, collection: Iterable):
    return item in collection


print(contains('a', "eshmat"))