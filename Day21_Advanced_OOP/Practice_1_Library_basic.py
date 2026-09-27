#Program 1: Library_Basid.py
print("Program 1: Library Basics ")

class Book:
    def __init__(self, title , author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title} \n Author: {self.author}")

class Library:
    def __init__(self):
        self.books_list = []

    def add_book(self):
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        book = Book(title,author)

        if not title or not author:
            print("title and author can't be empty")
        else:
            self.books_list.append(book)

            print("Book added successfully!")


    def view_books(self):
        if  not  self.books_list:
            print('Book not available!')
            return

        print("----- Books List ------")
        for book in self.books_list:
            book.display()
            print("----")

    def main_menu(self):
        while True:
              print("\nSelect Option: ")
              print("1. Add Book")
              print("2. View Books")
              print("3. Exit")

              try:
                 option = int(input("\nEnter your choice :"))
              except ValueError:
                print("choice should be integer!")
                continue

              if option == 1:
                 self.add_book()

              elif option == 2:
                 self.view_books()

              elif option == 3:
                  print("Exit")
                  break

              else:
                  print("Invalid option!")

manager = Library()
manager.main_menu()
