while True:
    try:
        n = int(input("Enter number: "))

        print("Rahmat bratim!")
        break
    except ValueError:
        print("Iltimos son kiriting")
        continue
    
