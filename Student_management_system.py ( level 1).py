#Mini Project: Student Data Management System (Level 1)
print("Mini Project: Student Data Management System (Level 1)")


def grade(marks):
    if marks >= 90:
        grade = "A"
        return grade

    elif marks >= 75:
        grade = "B"
        return grade

    elif marks >= 50:
        grade = "C"
        return grade

    else:
        grade = "Fail"
        return grade

def add_students(students_record):
        name= input("Enter your Name:")
        age = int(input("Enter your Age :"))
        marks =int(input("Enter your marks:"))

        if name in students_record:
            print(f"\nThe student {name} already exists!")
        else:
            g=grade(marks)
            students_record[name] =  {'Name' : name , 'Age' : age, 'Marks' :marks , 'Grade' : g}
            print( f" \nStudents Record = {students_record[name]} ")
            print("Student added successfully!")


def view_students(students_record):
    if students_record:
        print("\n--- Student Record ---")
        for name, details in students_record.items():
            print(f"\n{name}:")
            for key ,value in students_record.items():
                print(key ,":" , value)
    else:
        print("No Student found! ")


def search_students(students_record):
    if students_record:
        name = input("Enter name to search:")

        if name in students_record:
            print("\n--- Students Record ---")
            print(f"\nThe student {name} has found!")
            for key, value in students_record[name].items():
                print(f"{key}: {value}")
        else:
            print(f"the student {name} not found!")
            print("add student first")


def update_marks(students_record):
    name = input("Enter name to update marks: ")
    marks = int(input("Enter your marks:"))

    if name in students_record:
        new_marks = int(input("Enter new marks: "))
        students_record[name]["Marks"] = new_marks
        students_record[name]["Grade"] = grade(new_marks)
        print("Marks updated successfully!")
    else:
        print("Student not found.")


Students_record = {}

while True:
    print("\n----Welcome to Students Data Management System----")


    print("\nSelect options:\n"
          "1.Add Students:\n"
          "2.View all students\n"
          "3.search students\n"
          "4.Update marks;\n"
          "5.Exit")


    choice = int(input("\nEnter your choice:-"))

    if choice == 1:
       add_students(Students_record)

    elif choice == 2:
       view_students(Students_record)

    elif choice == 3:
       search_students(Students_record)

    elif choice == 4:
       update_marks(Students_record)

    elif choice == 5:
       print("Exiting the Program \n Thanks for Visiting!")
       break

    else:
        print("Invalid choice")







