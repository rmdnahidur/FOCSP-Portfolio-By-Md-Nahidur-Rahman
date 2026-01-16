'''
12.Write a program to implement a basic library book management with the functionalities such as issue the book, return the book and 
search the book. Use the concept of OOP to create the necessary classes on your own and implement the concept of other OOP features.
For the storage of book details, use the file handling along with the exception handling. 
'''

# Book class
class Book:
    def __init__(self, book_id, title, author, issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = issued

    # Convert book object to string for file storage
    def to_string(self):
        return f"{self.book_id},{self.title},{self.author},{self.issued}\n"

    # Create book object from string
    @staticmethod
    def from_string(data):
        parts = data.strip().split(",")
        return Book(parts[0], parts[1], parts[2], parts[3] == "True")

# Library class
class Library:
    def __init__(self, filename):
        self.filename = filename
        self.books = []
        self.load_books()

    # Load books from file
    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    self.books.append(Book.from_string(line))
        except FileNotFoundError:
            # File not found, create empty book list
            self.books = []

    # Save books to file
    def save_books(self):
        with open(self.filename, "w") as file:
            for book in self.books:
                file.write(book.to_string())

    # Add a new book
    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f"Book '{book.title}' added successfully!")

    # Search for a book by title
    def search_book(self, title):
        found = False
        for book in self.books:
            if title.lower() in book.title.lower():
                status = "Issued" if book.issued else "Available"
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")
                found = True
        if not found:
            print("Book not found!")

    # Issue a book by ID
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.issued:
                    book.issued = True
                    self.save_books()
                    print(f"Book '{book.title}' has been issued successfully!")
                else:
                    print(f"Book '{book.title}' is already issued.")
                return
        print("Book ID not found!")

    # Return a book by ID
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.issued:
                    book.issued = False
                    self.save_books()
                    print(f"Book '{book.title}' has been returned successfully!")
                else:
                    print(f"Book '{book.title}' was not issued.")
                return
        print("Book ID not found!")

# Main program
library = Library("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem12/books.txt")

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        new_book = Book(book_id, title, author)
        library.add_book(new_book)
    elif choice == "2":
        title = input("Enter Book Title to Search: ")
        library.search_book(title)
    elif choice == "3":
        book_id = input("Enter Book ID to Issue: ")
        library.issue_book(book_id)
    elif choice == "4":
        book_id = input("Enter Book ID to Return: ")
        library.return_book(book_id)
    elif choice == "5":
        print("Exiting Library Management System...")
        break
    else:
        print("Invalid choice! Please enter a valid option.")

