class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
        
    def return_book(self):
            if self._is_checked_out:
                self._is_checked_out = False
    
 
class Library(Book):
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        
        
        
    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(f"{book.title} by {book.author}")
        

    def check_out_book(self, book_title):
        for book in self._books:
            if book_title == book.title and not book._is_checked_out:
                book.check_out()
        

    def return_book(self, book_title):
        for book in self._books:
            if book_title == book.title and book._is_checked_out:
                book.return_book()


    