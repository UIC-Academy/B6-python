class Counter:
    def __init__(self, count=0):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > 10:
            raise StopIteration
        return self.count


c = Counter()

# print(next(c))
# print(next(c))
# print(next(c))

for i in c:
    print(i)
