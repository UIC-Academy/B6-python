class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __eq__(self, other):
        is_equal = (self.title == other.title) and (self.author == other.author)
        return is_equal
        
    def __str__(self):
        return f"Book<title={self.title}>"
    
b1 = Book(
    "Molxona",
    "Jorj Oruell"
)
b3 = Book(
    "Molxona",
    "Jorj Oruell"
)

b2 = Book(
    "Start With Why",
    "Simon Sinek"
)

print(b1 == b3)