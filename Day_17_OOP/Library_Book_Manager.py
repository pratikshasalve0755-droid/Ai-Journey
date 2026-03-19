# Mini Project : Library Book Manager (OOP version)
print(" Mini Project : Library Book Manager (OOP version)")

class Book:
    def __init__(self,title, author,year):
        self.title = title
        self.author = author
        self.year = year


    def display(self):
        print("----------------------------")
        print("Title:" , self.title)
        print("Author: " , self.author)
        print("Year:" , self.year)
        print("----------------------------")


class LibraryManager:
    def __init__(self):
        self.books_list = []

    def add_book(self, title,author,year):
        new_book = Book(title,author,year)
        self.books_list.append(new_book)
        print(f"The Book {title} added to the Library!")

    def view_all_books(self):
        if not self.books_list:
            print("No Book in Library.")
            return

        print("-------Library Books--------")
        for book in self.books_list:
            book.display()

    def search_book(self , title):
       found = False

       for book in self.books_list:
           if book.title.lower() == title.lower():
               book.display()
               print(f"Book of {title } title found!")
               found = True

       if not found:
           print(f"The Book ' {title}' not found!")

library = LibraryManager()

while True:
    print("\n-----Library Menu-----")
    print("Select Options:")
    print("1. Add Book :"
          "\n2. View All Books:"
          "\n3. Search Book: "
          "\n4. Exit")
    print("----------------------------")

    try:
       choice = int(input("\nEnter your choice:"))

    except ValueError:
        print("Enter Valid Choice!")
        continue

    if choice == 1:
            title = input("\nEnter title:").strip()
            author = input("Enter author name:").strip()
            try:
                 year = int(input("Enter published year:"))
            except ValueError:
                print("Invalid year!")
                continue

            library.add_book(title , author , year)

    elif choice == 2:
        #title = input("\nEnter title:").strip()
        library.view_all_books()

    elif choice == 3:
        title = input("\nEnter title:").strip()
        library.search_book(title)

    elif choice == 4:
        print("The Program Exit! , Thank you!")
        break

    else:
        print("Invalid choice! try again! ")








