def sum_args(*args: tuple[int]) -> int:
    if not args:
        return 0
    for i in args:
        if isinstance(i, str):
            print("String can't be used.")
            return -1
    
    return sum(args)

print(sum_args(2,3,4,5,6, "ddd"))
print(sum_args())