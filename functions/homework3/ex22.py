users = [
    ("Eshmat", 20),
    ("Toshmat", 21),
    ("Gulchapchap", 19),
]

sorted_users = sorted(
    users,
    key=lambda x: x[1]
)

print(sorted_users)