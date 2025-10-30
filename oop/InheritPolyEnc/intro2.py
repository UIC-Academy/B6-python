class Logger:
    def __init__(self, max_lines: int):
        self.max_lines = max_lines
    
    def log(self, msg: str):
        print(f"[LOG] {msg}")


class Saver:
    def __init__(self, is_db):
        self.is_db = is_db
    
    def save(self):
        print("Data saved.")
        

class MyApp(Logger, Saver):
    def __init__(self, max_lines):
        super().__init__(max_lines)
    
    def use(self):
        print("I'm using my app.")
        

app1 = MyApp(
    max_lines=12
)

app1.log("Salom")
app1.save()
app1.use()
print(app1.max_lines)
print(MyApp.__mro__)