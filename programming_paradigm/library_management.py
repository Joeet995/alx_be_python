class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self, book_title):
        if self.title == book_title:
            self._is_checked_out = True
        
    def return_book(self, book_title):
        if self.title == book_title:
            self._is_checked_out = False
    

class Library(Book):
    def __init__(self, title, author):
        super().__init__(title,author)
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        self.return_book(book)
        
        
    def list_available_books(self):
        for book in self._books:
            print(f"{self.title} by {self.author}")
        

    def check_out_book(self, book):
        self._books.remove(book)
        self.check_out(book)

    def return_book(self, book):
        self._books.append(book)
        super().return_book(book)


    