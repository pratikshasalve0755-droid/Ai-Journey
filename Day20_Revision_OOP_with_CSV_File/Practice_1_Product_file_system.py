#Program 1: Product_file_system.py
print("\nProgram 1: Product_file_system.py")

import csv
import os


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_list(self):
        return [self.name, self.price, self.quantity]


while True:
      Product_name = input("\nEnter name:")
      if  Product_name:
         break
      print("name is required ! , Please enter name")

while True:
      try:
         Product_price = float(input("Enter Price:"))
         if Product_price > 0:
             break
         else:
            print("Price cannot be zero or negative , Please enter Price!")

      except ValueError:
            print("Enter numerical value only!")

while True:
    try:

      Product_quantity = int(input("Enter quantity:"))
      if Product_quantity > 0  and Product_price > 0:
         break
      else:
        print("Quantity cannot be zero or negative , Please enter quantity!")

    except ValueError:
            print("Enter numerical value only!")


p1 = Product(Product_name, Product_price, Product_quantity)

file_exists = os.path.exists("product_record.csv")

with open("product_record.csv", "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
       writer.writerow(["Name ", "Price", "Quantity"])

    writer.writerow(p1.to_list())

print("Product added successfully!")



"""with open("product_record.csv" , "w" , newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name" , "Price" , "Quantity"])"""







