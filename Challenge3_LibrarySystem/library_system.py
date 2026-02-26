class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully!\n")

    def view_books(self):
        if not self.books:
            print("No books in library.\n")
            return

        print("\nLibrary Books:")
        for index, book in enumerate(self.books):
            status = "Issued" if book.is_issued else "Available"
            print(f"{index + 1}. {book.title} by {book.author} - {status}")
        print()

    def issue_book(self):
        self.view_books()
        choice = int(input("Enter book number to issue: ")) - 1

        if 0 <= choice < len(self.books):
            if not self.books[choice].is_issued:
                self.books[choice].is_issued = True
                print("Book issued successfully!\n")
            else:
                print("Book already issued.\n")
        else:
            print("Invalid choice.\n")

    def return_book(self):
        self.view_books()
        choice = int(input("Enter book number to return: ")) - 1

        if 0 <= choice < len(self.books):
            if self.books[choice].is_issued:
                self.books[choice].is_issued = False
                print("Book returned successfully!\n")
            else:
                print("This book was not issued.\n")
        else:
            print("Invalid choice.\n")


library = Library()

while True:
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        library.issue_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.\n")
