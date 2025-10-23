import os
import time


print(os.getcwd())
# os.chdir("../")
# print(os.getcwd())
print(os.listdir(os.pardir))
print(os.name)
print(os.path.join("section2", "file.txt"))
print(os.path.basename("/home/voidp/Desktop/tasks.md"))
print(os.path.dirname("/home/voidp/Desktop/tasks.md"))
print(os.path.exists("/home/voidp/Documents"))
print(os.path.isdir("/home"))
print(os.path.isfile("./file.txt"))
try:
    os.remove("./file.txt")
except FileNotFoundError:
    print("Fayl topilmadi.")

os.mkdir("./test_dir")
print(os.path.exists("./test_dir"))
print("Waiting for 5 seconds...")
time.sleep(5)
os.rmdir("./test_dir")
print(os.path.exists("./test_dir"))

os.rename("./exercises.md", "./mashqlar.md")

# path - file yoki directoryning manzili, borish yo'li
# file - ma'lumot saqlanadigan xotira birligi
# directory - bir nechta fayllarni guruhlab ushlab turish imkonini beradi