# MINI PROJECT : Smart Student Database System
print("\nMINI PROJECT: SMART STUDENT DATABASE SYSTEM")


import os
import json

FILENAME = "students.json"

def load_students():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r" , encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("\nError while Reading the json file!")
            return []
    return []

def save_students(students):
    with open(FILENAME , "w")as file:
        json.dump(students,file , indent=4)


def add_student():
    students = load_students()
    student = {
        "id": int(input("Enter Student Id:")),
        "name": input("Enter Student Name:"),
        "age": int(input("Enter Student Age:")),
        "course": input("Enter Course"),
        "city": input("Enter City:")

    }

    if not student["name"].strip() == " ":
        print("The Name can't be empty!")

    students.append(student)

    for s in students:
        if s["id"] == student["id"]:
            print("Student ID already exists!")
            return
    students.append(student)
    save_students(students)
    print(f"\nStudent Data Added Successfully! in {FILENAME}")

def view_students():

    students = load_students()
    if not students :
        print("No Student Found!")
        return

    print("\n===== Smart Student Database System =====")
    for student in students:
        print("-------------------------------")
        print("Student ID :", student["id"])
        print("Name : ", student["name"])
        print("Age :", student["age"])
        print("Course : ", student["course"])
        print("City :", student["city"])
        print("-------------------------------")
def search_student():

    students = load_students()

    try:
        stu_id = int(input("Enter id:"))
    except ValueError:
        print("Invalid Id!")
        return
    found = False

    for student in students:

        if student["id"] == stu_id:
            found = True
            print("\n===== Smart Student Database System =====")
            print("Student ID :", student["id"])
            print("Name : ", student["name"])
            print("Age :", student["age"])
            print("Course : ", student["course"])
            print("City :", student["city"])
            break

    if not found:
        print("No Student Found!")

def update_student():
    students = load_students()

    try:
        stu_id = int(input("Enter Student Id want to be update:"))

    except ValueError:
        print("Invalid Id!")
        return

    found = False
    for stu in students:
        if stu["id"] == stu_id:
            found = True
            stu["name"]= input("Enter Student Name:")
            stu["age"]= int(input("Enter New Age"))
            stu["course"]= input("Enter New Course:")
            stu["city"]= input("Enter New City:")
            break

    if found:
       save_students(students)
       print("\nStudent Data Updated Successfully!")

    else:
        print("Student Not Found!")

def delete_student():

    students = load_students()
    try:
        stu_id = int(input("Enter Student id:"))

    except ValueError:
        print('Invalid Id!')
        return

    found = False

    for stu in students:
        if stu["id"] == stu_id:
            found = True
            students.remove(stu)
            save_students(students)
            print("\nData deleted Successfully")
            break

    if not found:
        print("No Student Found!")


while True:
    print("\n===== Smart Student Database System =====")
    print("Select Option:")
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student"),
    print("6. Exit")

    try:
        option = int(input("Choose an Option:"))

    except ValueError:
        print("Invalid Option!")
        continue

    if option == 1:
       add_student()

    elif option ==  2:
        view_students()

    elif option == 3:
       search_student()

    elif option == 4:
       update_student()

    elif option == 5:
       delete_student()


    elif option == 6:
       print("Existing........")
       break

    else:
        print("Invalid Option!")