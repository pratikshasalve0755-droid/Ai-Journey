# Mini app : Upgrade Budget Tracker
print("Mini app: Upgraded Budget Tracker System")

import csv
import os

def add_expenses():
   date = input("Enter Date (YYYY-MM--DD):-")

   category = input("Enter Category:- ")
   if not category.strip():
       print("category cannot be empty!")
       return

   try:
       amount = float(input("Enter Amount:-"))
   except ValueError:
       print("Enter valid number!")
       return

   description = input("Enter Description:-")

   file_exists = os.path.isfile("expenses.csv")

   with open("expenses.csv" , "a" , newline='') as file:
       csv_writer = csv.writer(file)

       if not file_exists:
           csv_writer.writerow(["Date" , "Category" , "Amount" , "Description"])

       csv_writer.writerow([date, category ,amount , description])

   print("Expenses Added Succesfully!")

def view_expenses():

    try:
        with open("expenses.csv" , "r") as file:
            csv_reader = csv.reader(file)

            next(csv_reader ,None)

            print("\n Date  | Category  | Amount  | Description ")
            print("---------------------------------------------------")

            for row in csv_reader:
                if len(row) >= 4:
                   print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

    except FileNotFoundError:
        print("File not Found")

def calculate_total():
    total = 0

    try:
        with open("expenses.csv" , "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader,None)

            for row in csv_reader:
                if len(row) >= 3:
                   total += float(row[2])

        print("Total Spending: Rs. " , total)

    except FileNotFoundError:
        print("No expenses recorded yet")

def category_totals():

    category_totals = {}

    try:
        with open("expenses.csv" , "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader , None)

            for row in  csv_reader:
                if len(row) >= 3:
                   category = row[1]
                   amount = float(row[2])

                   if category in category_totals:
                      category_totals[category] += amount
                   else:
                      category_totals[category] = amount

        print("Category-wise Spending :-" )
        print("-----------------------")

        for category , amount in category_totals.items():
            print(f" {category} : Rs: {amount}")

    except FileNotFoundError:
        print("Expenses File Not Found!")

def main_menu():

    while True:

        print("\n------ Welcome to Budget Tracker ------")
        print("1) Add Expense")
        print("2) View All Expenses")
        print("3) View Total Spending")
        print("4) View Category-wise Total")
        print("5) Exit")

        try:
            choice = int(input("\nEnter your choice:- "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            add_expenses()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            calculate_total()

        elif choice == 4:
            category_totals()

        elif choice == 5:
            print("Thanks for using Budget Tracker!")
            break

        else:
            print("Invalid menu choice. Please select 1-5.")


main_menu()
"""with open("expenses.csv" , "w" , newline="") as  file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['date' , 'category' ,'amount' , 'description'])"""
