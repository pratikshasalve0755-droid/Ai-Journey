#Program 3: Category_total

import csv

search_category = input("Enter category to search:- ")
total = 0

with open("expenses.csv","r") as file:
   csv_reader = csv.reader(file)
   next(csv_reader)

   for row in csv_reader:
       if row[1].lower() == search_category.lower():
           amount = float(row[2])
           total += amount
print("Total spending :-",total)




