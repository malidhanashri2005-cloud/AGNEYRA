# Library Management System (OOP Based)

class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.is_issued = False

    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print(f"Book '{self.title}' issued successfully.")
        else:
            print("Book is already issued.")

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print(f"Book '{self.title}' returned successfully.")
        else:
            print("Book was not issued.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def show_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f"ID: {book.book_id} | Title: {book.title} | Status: {status}")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.issue_book()
                return
        print("Book ID not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.return_book()
                return
        print("Book ID not found.")


# ---------------- MENU SYSTEM ---------------- #

def show_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")


library = Library()

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        book = Book(book_id, title)
        library.add_book(book)

    elif choice == '2':
        library.show_books()

    elif choice == '3':
        book_id = int(input("Enter Book ID to issue: "))
        library.issue_book(book_id)

    elif choice == '4':
        book_id = int(input("Enter Book ID to return: "))
        library.return_book(book_id)

    elif choice == '5':
        print("Exiting system...")
        break

    else:
        print("Invalid choice! Try again.")
