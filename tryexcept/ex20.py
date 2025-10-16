from typing import Callable

def dec(func: Callable):
    def wrapper(*args, **kwargs):
        for i in range(3):
            passwd = input("Enter password: ")
            try:
                func(passwd)
                break
            except PermissionError:
                if i < 2:
                    print("Incorrect Password, please try again!")
                else:
                    print("Too many attempts. You have been blocked!")
    return wrapper


@dec
def password_checker(passwd: str):
    if passwd != "supersecret":
        raise PermissionError("Incorrect Password")
    
    print("Tizimga xush kelibsiz!")


password_checker()