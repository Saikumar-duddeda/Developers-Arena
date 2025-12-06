# Library Management System using OOP - Week 5 Project

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True  # book is available by default

    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # list of book_ids

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Borrowed: {self.borrowed_books}"


class Library:
    def __init__(self):
        self.books = []      # list of Book objects
        self.members = []    # list of Member objects
        self.next_book_id = 1
        self.next_member_id = 1

    # Add a new book
    def add_book(self, title, author):
        book = Book(self.next_book_id, title, author)
        self.books.append(book)
        self.next_book_id += 1
        print(f"Book added: {book}")

    # Register a new member
    def add_member(self, name):
        member = Member(self.next_member_id, name)
        self.members.append(member)
        self.next_member_id += 1
        print(f"Member added: {member}")

    # Find book by ID
    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    # Find member by ID
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    # Borrow a book
    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None:
            print("Member not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if not book.is_available:
            print("Book is already borrowed.")
            return

        book.is_available = False
        member.borrowed_books.append(book.book_id)
        print(f"{member.name} borrowed '{book.title}'")

    # Return a book
    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None:
            print("Member not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if book_id not in member.borrowed_books:
            print("This member did not borrow that book.")
            return

        book.is_available = True
        member.borrowed_books.remove(book_id)
        print(f"{member.name} returned '{book.title}'")

    # Display all books
    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("\n=== Books in Library ===")
        for book in self.books:
            print(book)
        print()

    # Display all members
    def display_members(self):
        if not self.members:
            print("No members registered.")
            return

        print("\n=== Library Members ===")
        for member in self.members:
            print(member)
        print()


def main():
    library = Library()

    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Display All Books")
        print("4. Display All Members")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)

        elif choice == "2":
            name = input("Enter member name: ")
            library.add_member(name)

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            library.display_members()

        elif choice == "5":
            try:
                member_id = int(input("Enter member ID: "))
                book_id = int(input("Enter book ID: "))
                library.borrow_book(member_id, book_id)
            except ValueError:
                print("Invalid input. IDs must be numbers.")

        elif choice == "6":
            try:
                member_id = int(input("Enter member ID: "))
                book_id = int(input("Enter book ID: "))
                library.return_book(member_id, book_id)
            except ValueError:
                print("Invalid input. IDs must be numbers.")

        elif choice == "7":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
