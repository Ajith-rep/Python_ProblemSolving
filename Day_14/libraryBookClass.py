class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []   # list of Book objects

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print(f"Book borrowed: {book.title}")
                else:
                    print(f"Book not available: {book.title}")
                return
        print("Book not found")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.available = True
                print(f"Book returned: {book.title}")
                return
        print("Book not found")

    def display_books(self):
        print("\nBooks in Library:")
        for book in self.books:
            book.display()

b1 = Book("Atomic Habits", "James Clear", "111")
b2 = Book("Ikigai", "Héctor García", "222")

lib = Library("City Library")
lib.add_book(b1)
lib.add_book(b2)

lib.borrow_book("111")   # borrow
lib.borrow_book("111")   # trying again (not available)
lib.return_book("111")   # return
lib.display_books()      # show all books
