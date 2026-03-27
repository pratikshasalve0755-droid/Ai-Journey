#Program 3: Product_search.p
print("Program 3: Product_search.py")

import csv

name = input("Enter name to search :").strip().lower()

try:
    with open("product_record.csv" , "r" , newline="") as file:
         reader = csv.reader(file)
         next(reader, None)

         found = False

         for row in reader:
            if len(row) < 3:
                continue


            if name == row[0].lower():
                print("----- Product Details -----")
                print("---------------------------")
                print(f"Name: {row[0]}" )
                print(f"Price: {row[1]}")
                print(f"Quantity: {row[2]}")
                found = True
                break
         if not found:
             print("Product not Found!")

except FileNotFoundError:
    print("file does not Exists!")