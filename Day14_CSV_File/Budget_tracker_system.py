#Mini Project: Budget_Tracker_System

import csv
import os

while True:
    print("\n------Welcome to the Budget tracker System------")
    print("\nSelect Options:-\n" 
      "1) Add Expense \n"
      "2) View All Expenses \n"
      "3) View Total Spending \n"
      "4) View Category-wise Total \n"
      "5) Exit \n")

    try:
        choice = int(input("Enter your choice:- "))
    except ValueError:
        print("Please enter valid number!")
        continue

    if choice == 1:                                               #Add Expensses

       Date = input("Enter Date (YYYY-MM-DD):-")
       Category = input("Enter category:- ")
       Amount = float(input("Enter amount:- "))
       Description = input("Enter description:- ")

       file_exists = os.path.isfile("expenses.csv")

       with open("expenses.csv" , "a" ,newline= "") as file:
           csv_writer = csv.writer(file)
           if not file_exists :
               csv_writer.writerow(["Date","Category", "Amount" ,"Description"])
           csv_writer.writerow([Date, Category, Amount, Description])

       print("Expenses added successfully!")

    elif choice == 2:                                              #View all expenses
        try:
            with open("expenses.csv" , "r" ) as file:
               csv_reader = csv.reader(file)
               next(csv_reader)
               print("\nDate | Category | Amount | Description")
               print("--------------------------------------------")

               for row in csv_reader:
                   print(  f" {row[0]} | {row[1]} | {row[2]} | {row[3]} \n")
        except FileNotFoundError:
          print("Error: Expenses file not found!")

    elif choice == 3:
        total = 0

        try:
            with open("expenses.csv", "r") as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                for row in csv_reader:

                       total += float(row[2])

            print("Total Spending:-", total)

        except FileNotFoundError:
            print("No expenses recorded yet.")

    elif choice == 4:                                 #View Category-wise Total
        category_totals = {}

        try:
            with open("expenses.csv" , "r" ,newline="" ) as file:
                 csv_reader =csv.reader(file)
                 next(csv_reader,None)
                 for row in csv_reader:
                     category = row[1]               #assuming that category is at the 3rd postion
                     amount = float(row[2])                  #assuming that amount is at the 4th position

                     if category in category_totals:
                         category_totals[category] += amount
                     else:
                        category_totals[category] = amount
            print("\nCategory-wise Spending:")
            print("--------------------------")
            for category , total in category_totals.items():
               print(f"{category} : Rs.{total}")

        except FileNotFoundError:
            print("No expenses recorded yet.")

    elif choice == 5:
        print("Thank you for using Budget Tracker!")
        break

    else:
        print("Enter a invalid choice!")


"""with open("expenses.csv" , "w" , newline="") as  file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['date' , 'category' ,'amount' , 'description'])"""










