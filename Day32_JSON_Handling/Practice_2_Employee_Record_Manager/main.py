# Program 2: Employee Record Manager
print("\n Program 2: Employee Record Manager")

import os
import json

FILENAME = "employees.json"

def load_employees():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("\nError reading JSON file. Resetting data.")
            return []
    return []

def save_employees(employees):
    with open(FILENAME, "w") as file:
        json.dump(employees, file, indent=4)

while True:

    print("\nEmployee Record Manager")
    print("\nSelect an Option")
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    try:
        option = int(input("\nEnter option:"))

    except ValueError:
        print("Invalid Option!")
        continue


    if option == 1:

       employees = load_employees()
       employee = {
            "emp_id" : int(input("\nEnter Employee ID:")),
            "name" : input("Enter Employee Name:"),
            "dept" : input("Enter Department:"),
            "salary" : int(input("Enter Employee Salary:"))
    }


       employees.append(employee)
       save_employees(employees)
       print(f"Data Saved Successfully in {FILENAME}")

    elif option == 2:
       if not os.path.exists(FILENAME):
            print("File Doesn't Exists!")
            continue

       employees = load_employees()

       for emp in employees:
            print("\n=== Employee Record Manager ===")
            print("\nEmployee ID : " , emp["emp_id"])
            print("Employee Name : ", emp["name"]),
            print("Department :" , emp["dept"]),
            print("Salary:", emp["salary"])

    elif option == 3:
        print("Exiting...")
        break

    else:
        print("Invalid Option!")


