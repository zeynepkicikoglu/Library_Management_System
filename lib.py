class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0) #imleç dosyanın başına gider
        books = self.file.read().splitlines()
        if not books:
            print("No books in the library.")
        else:
            print("The list of books:")
            for book in books:
                print(f"Title: {book[0]}, Author: {book[3]}")

    def add_book(self):
        book_name = str(input("Enter the book title: "))
        author = str(input("Enter the author: "))
        release_year = str(input("Enter the release year: "))
        num_pages = str(input("Enter the number of pages: "))
        book_info = book_name + ", " + author + ", " + release_year + ", " + num_pages + "\n"
        self.file.write(book_info)
        print(f"Book '{book_name}' added successfully.")

    def remove_book(self):
        self.file.seek(0) #imleç dosyanın başına gider
        books = self.file.readlines()
        if not books:
            print("No books to remove in the library")
        else:
            book_name = input("Enter the title of the book to remove: ")
            updated_books = []
            found = False
            for book in books:
                if not book.startswith(book_name):
                    updated_books.append(book)
                else:
                    found = True
            if found:
                self.file.seek(0)
                self.file.truncate() #dosyanın yeni boyutunu tanımlar 
                self.file.writelines(updated_books)
                print(f"Book '{book_name}' removed successfully.")
            else:
                print(f"No book with title '{book_name}' found in the library.")



lib = Library("books.txt")
print("Welcome to the ZK's Library!\n")

while True:

    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")
    choice = str(input("Enter your choice: "))

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("You entered invalid choice. Please enter a number between 1 and 4: ")

