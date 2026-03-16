"""students = []                                         # initialize the list
n = int(input("\nEnter no of  students:"))

for _ in range(n):
    name = input("Enter name:")
    age = int(input("Enter age:"))
    marks = int(input("Enter marks:"))
    print("----------------------")
    student = {'name': name,'age': age , 'marks': marks}
    students.append(student)

    for student in students:

        print(f"student = Name: {student['name']} | Age: {student['age']} | Marks:{student['marks']}")"""
from dataclasses import asdict

"""import csv

search_category = input("Enter the category to search:- ")
total = 0

with open("expenses.csv", "r") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        if row[1].lower() == search_category.lower():
            amount = float(row[2])
            total += amount

print("Total spending for", search_category, "is:", total)"""

def add_member():

    name = input("Enter Name:-").lower()
    if name.strip() == "":
        print("Name cannot be empty!")
        return

    try:
        age = int(input("Enter Age:-"))
    except ValueError:
        print("Invalid Age!")
        return
    memberships = ["Basic" , "Premium" , "VIP"]

    membership = input("Enter type of Membership:-").lower()
    if memberships in membership:
        print(f"{name} choosen {memberships} membership ")
    if membership.strip() == "":
        print("Membership type cannot be empty!")
        return


    file_exists = os.path.isfile("members.csv")

    with open("members.csv" , "a" , newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([ "Name" , "Age" , "Membership"])
        writer.writerow([ name , age ,  membership ])

    print("Members file added succesfully!")

name = "aaa"
age =22
membership = "Basic"

add_member()