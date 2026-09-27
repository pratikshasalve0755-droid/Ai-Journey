# Program 1: simple book class
print("\nProgram 1: Simple Book Class ")

class Book:
    def put_data(self):
        self.title = input("\nEnter Book Title:")
        self.author = input("Enter Author of Book:")
        self.price = input("Enter Price of Book: ")

    def display(self):
        print("----------------------------")
        print("Title:" , self.title)
        print("Author:" , self.author)
        print("Price: ", self.price)
        print("----------------------------")

b1 = Book()
b1.put_data()
b1.display()

b2 = Book()
b2.put_data()
b2.display()

print("--------------------------------------------------------------------------")

class Book:
    def put_data(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("----------------------------")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price: ", self.price)
        print("----------------------------")

b1 =Book()
title = input("\nEnter Book title:")
author = input("Enter Author of Book: ")
price = input("Enter Price of Book:")
b1.put_data(title , author , price)
b1.display()
