

def calculate(*args, operation="sum"):
    if operation == "sum":
        return sum(args)
    elif operation == "multiply":
        m = 1
        for i in args:
            m *= i
        return m
    
print(calculate(1, 2, 3 ,4, 5, operation="multiply"))