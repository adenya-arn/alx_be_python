class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        self.__is_checked_out = True

    def return_book(self):
        self.__is_checked_out = False

    def is_checked_out(self):
        return self.__is_checked_out

class Library:

    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)        

    def Check_out_Book(self, title):
        for book in self.__books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                return
            
            print(f"{title} is not available for checkout.")
        

    def Return_Book(self,title):
        for book in self.__books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                return
        print(f"{title} was not checked out.")        
    

    def list_available_books(self):
        available_books = [book for book in  self.__book if not book.is_checked_out()]
        for book in available_books:
            print(f"{book.title} by {book.author}")
