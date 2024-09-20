

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class User:
    def __init__(self, id, last_name):
        self.id = id
        self.last_name = last_name
        self.borrowed_books = []

class Library:
    books = []
    users = []
    
    def __init__(self):
        pass

    def add_book(self, title, author):
        new_book = Book(title, author)
        Library.books.append(new_book)
        print(f"Book '{title}' by {author} has been added to the library.")

    def add_user(self, id, last_name):
        new_user = User(id, last_name)
        Library.users.append(new_user)
        print(f"User {id} - {last_name} has been added to the library.")

    def borrow_book(self, user_id, book_title):
        for user in Library.users:
            if user.id == user_id:
                for book in Library.books:
                    if book.title == book_title and book.is_available:
                        book.is_available = False
                        user.borrowed_books.append(book)
                        print(f"Book '{book_title}' has been borrowed by user {user_id} - {user.last_name}.")
                        return
                print(f"Book '{book_title}' is not available.")
                return
        print(f"User {user_id} does not exist.")

    def return_book(self, user_id, book_title):
        for user in Library.users:
            if user.id == user_id:
                for book in user.borrowed_books:
                    if book.title == book_title:
                        book.is_available = True
                        user.borrowed_books.remove(book)
                        print(f"Book '{book_title}' has been returned by user {user_id} - {user.last_name}.")
                        return
                print(f"User {user_id} does not have book '{book_title}'.")
                return
        print(f"User {user_id} does not exist.")

def main():
    library = Library()
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Add User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == "2":
            id = input("Enter user ID: ")
            last_name = input("Enter user last name: ")
            library.add_user(id, last_name)
        elif choice == "3":
            user_id = input("Enter user ID: ")
            book_title = input("Enter book title: ")
            library.borrow_book(user_id, book_title)
        elif choice == "4":
            user_id = input("Enter user ID: ")
            book_title = input("Enter book title: ")
            library.return_book(user_id, book_title)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
