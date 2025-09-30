l = [i**2 for i in range(1, 11)]

words = ["eshmat", "toshmat", "hi", "hello", "waaa", "gulchapchap"]

res = [word if len(word) > 5 else word[::-1] for word in words]

res = [word.upper() for word in words]

print(res)

# List Comprehension
# Shorthand if / shorthand for