#Program 1: Write_expenses

import csv

Date = input("Enter Date (YYYY-MM-DD):- ")
Category = input("Enter Category:- ")
Amount = float(input("Enter Amount:- "))
Description = input("Enter description:- ")

file_exists = False
try:
    with open("expenses.csv" , "a" , newline="") as  file:
        file_exists = True
except FileNotFoundError:
    pass

with open("expenses.csv" , "a" ,newline="") as file:
    csv_writer = csv.writer(file)
    if not file_exists:
        csv_writer.writerow (["\nDate" ,"Category" ,"Amount" , "Description"])
    csv_writer.writerow([Date,Category,Amount,Description])

print("Expense added succesfully!")