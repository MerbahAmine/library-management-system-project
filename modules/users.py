from abc import ABC, abstractmethod
from book import Book

class User(ABC):
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books: list[Book] = []

    @abstractmethod
    def get_user_info(self) -> str:
        pass

    @abstractmethod
    def borrow_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def return_book(self, book: Book) -> None:
        pass


class Reader(User):
    def __init__(self, name: str):
        super().__init__(name)

    def get_user_info(self) -> str:
        return f"Reader: {self.name}, Borrowed: {[b.title for b in self.borrowed_books]}"

    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


class Librarian(User):
    def __init__(self, name: str):
        super().__init__(name)

    def get_user_info(self) -> str:
        return f"Librarian: {self.name}"

    def borrow_book(self, book: Book) -> None:
        # Librarian may not borrow, but let’s allow it for now
        self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def isAV(self, book:Book):
        if book.title == "amine":
           return f"ALooooooooor"
    
i=  Librarian("AMMMMRa")
print(i.isAV(Book("amine","omar","HJKL")))