def invert(
    l: list[int]
):
    # try:
    res = [n**(-1) for n in l]
    # except ZeroDivisionError:
    #     print("Listingizda nol bor ekan.")
    #     return []

    return res


print(invert([1,2,3,4,5]))
print(invert([1,0,2,3,4]))