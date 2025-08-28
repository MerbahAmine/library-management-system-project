from modules.bibliotheque import Bibliotheque
from modules.book import Book
from modules.users import User
from exception.costum_exception import Bibexception

class LibraryManagement:
    def __init__(self, bibliotheque: Bibliotheque)->None:
        self.bibliotheque= bibliotheque


    def chekout (self, title:str,user:User)->Book | None:
        book =  self.Bibliotheque.findBook(title)
        if book == None:
           raise Exception(Bibexception.BookNotFound())
        if not book.is_book_available:
            pass
        book.is_book_available = False
        user.borrow_book(book) 
        print(f"user{user.name} checked out the book {book.title}")
