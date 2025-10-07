x = 10


def show_number():
    x = 5  # shadowing
    print(x)
    
def change_number():
    global x
    x = 1000

show_number()
change_number()
print(x)


def outer():
    x = "tashqi"
    def inner():
        nonlocal x
        x = "ichki"
        print("Ichki x:", x)
    inner()
    
    print("Tashqi x:", x)

print(type(outer))
print(x)