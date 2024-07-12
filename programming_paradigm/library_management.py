class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = True

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title):
        self._books.append(title)
        self._is_checked_out = False

    def check_out_book(self, title):
        self._books.remove(title)
        self._is_checked_out = True
    
    def retun_book(self,title):
        self._books.append(title)
        self._is_checked_out = False

    def list_available_books(self):
        print(self._books)

