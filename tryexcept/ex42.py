def retry_on_failure(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                func()
            except ValueError as err:
                if i == 2:
                    raise ValueError(f"Couldn't execute the function for the {i+1}th time: ", err)
                print(f"Couldn't execute the function for the {i+1}th time...")

    return wrapper


@retry_on_failure
def myfunc():
    raise ValueError("Eshmat nima gap?")

myfunc()