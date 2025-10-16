try:
    f = open("hello.txt", "r")
    
    print(f.read())
except FileNotFoundError:
    print("Fayl topilmadi!")
finally:
    f.close()