class Book:
    def __init__(
        self, 
        name: str, 
        author: str, 
        isbn: str, 
        year: int
    ) -> None:
        self.name = name
        self.author = author
        self.isbn = isbn
        self.year = year
        
    def __str__(self) -> str:
        return f"Book<name={self.name}, author={self.author}, isbn={self.isbn}, year={self.year}>"
    
b1 = Book(
    name="Designing Data Intensive Applications",
    author="Martin Klemp",
    isbn="978-1-111-11111-1",
    year=2013
)

b2 = Book(
    name="5-sinf musiqa",
    author="Dilshod",
    isbn="978-1-222-22222-2",
    year=2015
)

print(b1, b2)