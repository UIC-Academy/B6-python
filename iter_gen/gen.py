def even(n: int):
    for i in range(n):
        if i % 2 == 0:
            yield i

n = 10

even_gen = even(10)
even_gen2 = even(20)

print(even_gen)
print(next(even_gen))
print(next(even_gen))
print(next(even_gen))


for i in even_gen:
    print(i)
    
# for i in even_gen2:
#     print(i)