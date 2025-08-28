class BookNotFound(Exception):

    def __init__(self, book_title: str) -> None:
         super().__init__(f"The book '{book_title}' is currently not available")
    
class BookNotAvailable(Exception):
      def BookNotFound(self)->Exception:
         print("THe error from not found")


#NB: A revoir c'est pas final
