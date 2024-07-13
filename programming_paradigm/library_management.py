class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def checkout_book(self, book_title):
        if self.title == book_title:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self, book_title):
        if self.title == book_title:
            self._is_checked_out = False
            return True
        return False

class Library(Book):
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        self.return_book(book)
        
    def list_available_books(self):
        available_books = [book for book in self._books]
        for book in available_books:
            print(f"{book} ")

    def checkout_book(self, book_title):
        self._books.remove(book_title)
        self.checkout_book(book_title)

    def return_book(self, book_title):
        self._books.append(book_title)
        self.return_book(book_title)
    


