class MyList:
    def __init__(self, jump_by: int, array: list[int] = [1, 2, 3, 6, 7, 8, 9, 10]):
        self.jump_by = jump_by
        self.idx = (-1) * self.jump_by
        self.array = array

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += self.jump_by
        if self.idx >= len(self.array):
            raise StopIteration
        return self.array[self.idx]


l = [i for i in range(0, 51)]
ml = MyList(5, l)

for i in ml:
    print(i)
