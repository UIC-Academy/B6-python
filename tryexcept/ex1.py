try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print(a / b)
except ZeroDivisionError:
    print("Nolga bo'lish mumkin emas!")
except ValueError:
    print("Iltimos faqat raqam kiriting!")