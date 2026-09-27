# Program 3: Book_class  with __str__ method
print("\nProgram 3: Book class  with __str__ method")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'The "{self.title}" written by "{self.author}"'
print("\n")
book1 = Book("Annihilation of Caste" , "Dr. Br. Ambedkar")
book2 = Book("Inheritance of loss" , "Kiran desai")

print(book1)
print(book2)