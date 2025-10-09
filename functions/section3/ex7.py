def create_multiplier(n):
    def inner(x) -> int:
        # nonlocal n
        return x * n
    
    return inner


multiplier_by_2 = create_multiplier(2)
multiplier_by_3 = create_multiplier(3)

n = int(input("Enter multiplier: "))
multiplier_by_n = create_multiplier(n)

print(multiplier_by_2(5))
print(multiplier_by_3(100))
print(multiplier_by_n(90))


"""
Closure - bir funksiya boshqa bir funksiya qaytarsa
"""