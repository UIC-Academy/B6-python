dc = {
    "name": "Eshmat",
    "age": 19,
    "city": "Tashkent"
}


try:
    key = input("Enter key: ")
    print(dc[key])
except KeyError as e:
    print("Bunday kalit topilmadi:", e)