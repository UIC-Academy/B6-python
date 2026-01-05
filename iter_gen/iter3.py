import pathlib


class MyFileIterator:
    def __init__(self, filename: str, key: str):
        self.filepath = pathlib.Path(pathlib.Path.cwd() / filename)
        self.key = key
        self.cur_line_idx = -1

        with open(self.filepath, "r") as f:
            self.lines = f.readlines()

    def __iter__(self):
        return self

    def __next__(self):
        self.cur_line_idx += 1
        while self.cur_line_idx < len(self.lines):
            if self.key in self.lines[self.cur_line_idx]:
                return self.lines[self.cur_line_idx]
            break
        if self.cur_line_idx >= len(self.lines):
            raise StopIteration


myfileparser = MyFileIterator("myfile.txt", "salom")

for salomline in myfileparser:
    if salomline:
        print(salomline, end="")
    else:
        continue
