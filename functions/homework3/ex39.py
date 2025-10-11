l = [1,5,3,7,6,9,2,4, 15]

fizzBuzzFunc = lambda n: print("FizzBuzz") if n % 3 == 0 and n % 5 == 0 else (print("Fizz") if n % 3 == 0 else print("Buzz"))

for n in l:
    fizzBuzzFunc(n)
    
