class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
    def __str__(self):
        return f"Book Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.is_available}"

class  LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
    def borrow_book(self,book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available for borrowing.")
    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} doesn't have '{book.title}' to return.")
    def __str__(self):
        return f"Member ID: {self.member_id},Name: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

class Library:
    def __init__(self,name):
        self.name = name
        self.book = []
        self.members = []
        self.transaction = []
    def add_book(self,book):
        self.book.append(book)
        print(f"Book '{book.title}' added to the library")
    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library.")
    def issue_book(self, book, member):
        if book in self.book and member in self.members:
            member.borrow_book(book)
            self.transaction.append(f"Issue: {member.name} borrowed '{book.title}'")
        else:
            print("Error: Either book or member not found.")
    def return_book(self,book,member):
        if book in self.book and member in self.members:
            member.return_book(book)
            self.transaction.append(f"Return: {member.name} returned '{book.title}'")
        else:
            print("Error: Either book or member not found")

    def show_books(self):
        print("\nList of Books in the Library:")
        for book in self.book:
            print(book)

    def show_members(self):
        print("\nList of Members in the Library:")
        for member in self.members:
            print(member)

    def show_transactions(self):
        print("\nList of Transactions:")
        for transaction in self.transaction:
            print(transaction)

my_library = Library("city Library")
book1 = Book("the great gatsby","f.scott Fitzgerald", "123456789")
book2 = Book("1984", "George Orwell", "987654321")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "456789123")
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

member1 = LibraryMember(1, "Patel")
member2 = LibraryMember(2, "john doe")
my_library.add_member(member1)
my_library.add_member(member2)

my_library.issue_book(book1, member1)
my_library.issue_book(book2, member2)


my_library.show_books()
my_library.show_members()

my_library.return_book(book1, member1)
my_library.return_book(book2, member2)

my_library.show_transactions()
