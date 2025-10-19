from typing import Callable

def dec(func: Callable):
    cnt = 0
    def wrapper(*args, **kwargs):
        nonlocal cnt
        
        try:
            res = func(passwd)
            return res
        except PermissionError:
            cnt+=1
            if cnt < 3:
                print("Incorrect Password, please try again!")
            else:
                print("Too many attempts. You have been blocked!")
    return wrapper


@dec
def password_checker(passwd: str):
    if passwd != "supersecret":
        raise PermissionError("Incorrect Password")
    
    return True



for i in range(3):
    passwd = input("Enter password: ")
    
    if password_checker(passwd=passwd):
        break

print("Tizimga xush kelibsiz!")