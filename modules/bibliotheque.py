from book import Book
from users import User

class Bibliotheque:
  def __init__(self,name):
    self.name = name
    self.users:list[User] = []
    self.books:list[Book] = []

  def addBook(self, book:Book)->None:
    self.books.append(book)

  def addUser(self, user:User):
    self.users.append(user)

  def findBook(self, title)->None:
      for b in self.books:
         if b.title == title:
             return b
        #return None
   
  def deletBook(self, book:Book):
       l =[]
       l += [book.title]
       print("from the liste LLL", l)
       raise ValueError("hello its fine muy is amine")
       self.books.remove(book)
  
  def ListBok(self):
     # self.addBook(Book("TM", "amine", "445I"))
      for b in self.books:
        if b.title !="M":
            self.deletBook(b)
            print("aLLLLO FROM 3")
        print(b)
             

lab = Bibliotheque("LAB1")
lab.addBook(Book("Ml", "amine", "445I"))
lab.addBook(Book("M", "amine", "445I"))
lab.addBook(Book("M", "amine2", "445I"))
lab.addBook(Book("Myhero3", "amine3", "445I"))


lab.ListBok()

