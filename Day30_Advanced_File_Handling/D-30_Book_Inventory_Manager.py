#Program 2: Book Inventory Manager
print("Program 2: Book Inventory Manager")

import os

filename = "books.txt"

if os.path.exists(filename):
    print("Student Notes Manager: File Exists")

else:
    print("Student Notes Manager: File Does Not Exists")


def add_books():
    book_id = int(input("Enter Book Id:"))
    book_name = input("Enter Book Name:")
    author = input("Enter Author Name:")
    quantity = int(input("Enter Quantity:"))

    with open(filename , "a" , encoding="utf-8") as file:
        file.write(f"    {book_id}    |    {book_name}    |    {author}    |    {quantity} \n")

    print("Book Added Successfully!")

def view_books():
    if not os.path.exists(filename):
        print("Student Notes Manager: File Does Not Exists")
        return

    with open(filename , "r") as file:
        book = file.read()

    if book.strip() == "":
        print("No books added!")

    else:
        print("--------------------- Book Inventory -----------------------")
        print(book)
        print("------------------------------------------------------------")


def search_books():
    if not os.path.exists(filename):
        print("Student Notes Manager: File Does Not Exists")
        return


    search_type = int(input("\nSearch using: \n1.Book Id  \n2.Book Name \n Enter Choice:"))

    found = False

    with open(filename , "r" , encoding="utf-8") as file:

            for line in file:

                book_id , book_name , author , quantity = line.strip().split("|")

                book_id = book_id.strip()
                book_name = book_name.strip()
                author = author.strip()
                quantity = quantity.strip()

                if search_type == 1:
                    user_book_id = int(input("\nEnter Book Id:"))

                    if user_book_id == book_id:
                       print("Book Found!")
                       print(f"\nBook ID : {book_id}")
                       print(f"Book Name : {book_name}")
                       print(f"Author : {author}")
                       print(f"Quantity : {quantity}")

                       found = True
                       break

                elif search_type == 2:
                    user_book_name = input("Enter Book Name:").strip()


                    if user_book_name == book_name:
                       print("Book Found!")
                       print(f"\nBook ID : {book_id}")
                       print(f"Book Name : {book_name}")
                       print(f"Author : {author}")
                       print(f"Quantity : {quantity}")

                       found = False
                       break

    if not found:
       print("Book not found!")


while True:
    print("\n=== Book Inventory Manager ===")
    print("\nSelect an choice:")
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")
    try:
        choice =int(input("\nEnter Your Choice:"))

    except ValueError:
        print("Invalid Choice")
        continue

    if choice == 1:
        add_books()

    elif choice == 2:
        view_books()

    elif choice == 3:
       search_books()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")
        """

with open(filename, "w", encoding="utf-8") as file:
    pass
"""





