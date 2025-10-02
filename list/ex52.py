"""
Join a list of words into a single string with spaces in between.
"""

l = ["hello", "eshmat", "qalesan"]

s = "-".join(l)

s2 = "-".join([l[0][:2], l[0][2:]])

print(s, s2)
