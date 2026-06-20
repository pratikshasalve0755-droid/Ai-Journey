# Mini Project: Library_Management_system_adv_oop.py
print("Mini Project : Library Management System ")

class Book:
    def __init__(self , title , author ):
        self.title = title
        self.author = author
        self.is_issued = False


class Member:
    def __init__(self , name ):
        self.name = name
        self.issued_books = []

class LibraryManager:
    def __init__(self):
        self.books_list = []
        self.members_list = []


    def add_book(self):

        title = input("Enter Book Title:")
        author = input("Enter Author Name:")

        if not title or not author:
            print("Title and Author is required!")
            return

        self.books_list.append(Book(title ,author ))
        print("Book added successfully!")

    def view_books(self):
            if not self.books_list:
                print("No Books Available")
                return

            for book in self.books_list:
                status = "Issued" if book.is_issued else "Available"
                print(f"Title : {book.title} ")
                print(f"Author : {book.author}")
                print(f"status : {status}")
                print("-------------------")

    def add_member(self):
        name = input("Enter Member Name:").strip()
        if not name:
            print("Name not found!")
            return

        self.members_list.append(Member(name))
        print("Member added successfully!")

    def issue_books(self):
        name = input("Enter Member Name:").strip()
        title = input("Enter Book Title:").strip()

        member = None
        for m in self.members_list:
            if m.name.lower() == name.lower():
              member = m
              break

        if not member :
           print("Member not found!")
           return

        book = None
        for b in self.books_list:
            if b.title.lower() == title.lower():
               book = b
               break

        if not book:
            print("Book not Found !")
            return

        if book.is_issued:
            print("Book already issued!")
            return

        book.is_issued = True
        member.issued_books.append(book)
        print("Book Issued successfully!")

    def return_book(self):
        name = input("Enter Member Name :").strip()
        title = input("Enter Book title :").strip()

        for member in self.members_list:
            if member.name.lower() == name.lower():
                for book in member.issued_books():
                    if book.title.lower() == title.lower():
                        member.issued_books.remove(book)
                        book.is_issued = False
                        print("Book returned successfully!")
                        return
                print("Book not found in member's list! ")
                return
        print("Member not found!")

    def view_member_books(self):
        name = input("enter member Name :").strip()

        for member in self.members_list:
            if member.name.lower() == name.lower():
                if not member.issued_books:
                    print("No book issued")
                    return

                print("\n Books issued:")
                for book in member.issued_books:
                    print(f"{book.title} by {book.author}")
                    return
        print("Member not found!")

                
    def main_menu(self):
        while True:
            print("\nSelect Option:")
            print("1. Add Book ")
            print("2. Add Member ")
            print("3. Issued Books ")
            print("4. Return Book ")
            print("5. View Books")
            print("6. View Member Books")
            print("7. Exit")
            print("--------------------")
            try:
                choice = int(input("Enter Your Choice:"))
            except ValueError:
                print("Invalid Value!")
                continue

            if choice == 1:
                self.add_book()

            elif choice == 2:
                self.add_member()

            elif choice == 3:
                self.issue_books()

            elif choice == 4:
                self.return_book()

            elif choice == 5:
                self.view_books()

            elif choice == 6:
                self.view_member_books()


            elif choice == 7:
                print("Exit!")
                break

            else:
                print("Invalid choice!")


manager = LibraryManager()
manager.main_menu()












