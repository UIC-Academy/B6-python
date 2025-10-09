#Define a function average(*numbers) that returns the average of any count of numbers.
def average(*numbers):
    if len(numbers) == 0:
     return 0
    return sum(numbers) / len(numbers)
print(average(1,2,3,4,5,6,7,8,9,10))