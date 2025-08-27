class Book:
    def __init__(self, title: str, author: str, ISBN: str):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_book_available = True   # default: available

    def __str__(self):
        status = "Available" if self.is_book_available else "Borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.ISBN}) - {status}"

 
b = Book("amine","omar",'34RTE')

print(b.__str__())