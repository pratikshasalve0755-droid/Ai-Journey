
# Mini Project: Expense Tracker (OOP + CSV)
print("Mini Project: Expenses Tracker (OOP + CSV")

import csv
import os


class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def to_list(self):
        return [self.date, self.category, self.amount, self.description]


class ExpenseManager:
    def __init__(self):
        self.file_name = "expenses.csv"

    def add_expense(self):
        date = input("Enter Date (YYYY-MM-DD): ").strip()
        category = input("Enter Category: ").strip()

        if not category:
            print("Category can't be empty!")
            return

        try:
            amount = float(input("Enter Amount: "))
        except ValueError:
            print("Invalid amount!")
            return

        description = input("Enter Description:  ").strip()

        expense = Expense(date, category, amount, description)

        file_exists = os.path.isfile(self.file_name)

        with open(self.file_name, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Date", "Category", "Amount", "Description"])

            writer.writerow(expense.to_list())

        print("Expense added successfully!")

    def view_expenses(self):
        try:
            with open(self.file_name, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader, None)

                print("\nDate       | Category | Amount   | Description")
                print("----------------------------------------")

                found = False

                for row in reader:
                    print(f"{row[0]} | {row[1]}     | {row[2]}    | {row[3]}")
                    found = True

                if not found:
                    print("No expenses found!")

        except FileNotFoundError:
            print("Expenses file not found!")

    def total_expenses(self):
        total = 0
        found = False

        try:
            with open(self.file_name, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader, None)

                for row in reader:
                    try:
                        total += float(row[2])
                        found = True
                    except ValueError:
                        continue

            if found:
                print("Total Expense:", total)
            else:
                print("No expenses found!")

        except FileNotFoundError:
            print("Expenses file not found!")

    def category_wise_expense(self):
        category_totals = {}

        try:
            with open(self.file_name, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader, None)

                for row in reader:
                    category = row[1].strip()

                    try:
                        amount = float(row[2])
                    except ValueError:
                        continue

                    if category in category_totals:
                        category_totals[category] += amount
                    else:
                        category_totals[category] = amount

            if category_totals:
                print("\nCategory-wise Expenses:")
                print("------------------------")
                for category, total in category_totals.items():
                    print(f"{category}: {total}")
            else:
                print("No expenses found!")

        except FileNotFoundError:
            print("Expenses file not found!")

    def main_menu(self):
        while True:
            print("\n------- Expense Tracker -------")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Total Expense")
            print("4. Category-wise Expenses")
            print("5. Exit")

            try:
                choice = int(input("\nEnter your choice: "))
            except ValueError:
                print("Invalid input!")
                continue

            if choice == 1:
                self.add_expense()

            elif choice == 2:
                self.view_expenses()

            elif choice == 3:
                self.total_expenses()

            elif choice == 4:
                self.category_wise_expense()

            elif choice == 5:
                print("Program exited. Thank you!")
                break

            else:
                print("Invalid choice!")


# Run program
manager = ExpenseManager()
manager.main_menu()




"""with open("expenses.csv" , "w" , newline="") as  file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['date' , 'category' ,'amount' , 'description'])"""