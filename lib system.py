class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have successfully borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently checked out.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Thank you for returning '{self.title}'.")
        else:
            print(f"'{self.title}' was not checked out.")

    def __str__(self):
        status = "Checked Out" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - [{status}]"


# --- Creating Book Objects and Testing the System ---

# Instantiate book objects
book1 = Book("1984", "George Orwell", "978-0451524935")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")

# Check initial status using __str__
print("--- Initial Library Inventory ---")
print(book1)
print(book2)
print(book3)
print()

# Test borrowing books
print("--- Borrowing Operations ---")
book1.borrow()  # Succeeds
book1.borrow()  # Fails (already borrowed)
book3.borrow()  # Succeeds
print()

# Check updated status
print("--- Updated Library Inventory ---")
print(book1)
print(book2)
print(book3)
print()

# Test returning books
print("--- Returning Operations ---")
book1.return_book()  # Succeeds
book2.return_book()  # Fails (wasn't borrowed)
print()

# Final status check
print("--- Final Library Inventory ---")
print(book1)