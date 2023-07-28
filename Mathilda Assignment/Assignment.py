class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Library:
    def _init_(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books:")
            for i, book in enumerate(self.books, 1):
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"{i}. {book.title} by {book.author} - {status}")

    def borrow_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'.")
            else:
                print("Sorry, the book is already borrowed.")
        else:
            print("Invalid book index.")

    def return_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned '{book.title}'.")
            else:
                print("You can't return a book that is not borrowed.")
        else:
            print("Invalid book index.")


def main():
    library = Library()

    while True:
        print("\nWelcome to the Library Management System")
        print("1. Add a book")
        print("2. Display available books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            library.add_book(title, author)
        elif choice == 2:
            library.display_books()
        elif choice == 3:
            library.display_books()
            book_index = int(input("Enter the index of the book to borrow: "))
            library.borrow_book(book_index)
        elif choice == 4:
            library.display_books()
            book_index = int(input("Enter the index of the book to return: "))
            library.return_book(book_index)
        elif choice == 5:
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if _name_ == "_main_":
    main()
