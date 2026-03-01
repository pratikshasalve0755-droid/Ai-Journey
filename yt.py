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
import csv

search_category = input("Enter the category to search:- ")
total = 0

with open("expenses.csv", "r") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        if row[1].lower() == search_category.lower():
            amount = float(row[2])
            total += amount

print("Total spending for", search_category, "is:", total)