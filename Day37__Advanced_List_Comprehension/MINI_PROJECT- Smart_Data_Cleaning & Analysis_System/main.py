#Mini Project : Smart Data Cleaning and Analysis System
print("\nMini Project : Smart Data Cleaning & Analysis System ")


students = [
    {"name": "Priti", "marks": 85},
    {"name": "", "marks": 72},
    {"name": "Rahul", "marks": 35},
    {"name": "Aarti", "marks": 91},
    {"name": " ", "marks": 48},
    {"name": "Vikas", "marks": 67},
    {"name": "Sneha", "marks": 78},
    {"name": "", "marks": 56},
    {"name": "Nakul", "marks": 93},
    {"name": "Kavya", "marks": 39}
]

clean_students_global = None


def get_clean_data():

    clean_students =[
        student
        for student in students
        if
        student["name"].strip() != ""
    ]

    return clean_students
def view_original_data():

    print("\nOriginal Data:")
    for student in students:
        print()
        print(f"Name   : {student['name']}")
        print(f"Marks : {student['marks']} ")
        print("---------------------------------------------------")



def clean_student_data():

     clean_list = get_clean_data()
     print("\n--------------- Cleaned Student Data ---------------")
     print()
     for s in clean_list:
         print(f"Name : {s['name']}  |   Marks : {s['marks']} ")



def show_passing_student():

    clean_list = get_clean_data()

    passing = [p for p in clean_list  if p['marks'] >= 40 ]

    print("\n-------- Passed Students ------------")
    print()
    for s in passing:
        print(f"Name : {s['name']}   |   Marks : {s['marks']} ")

def show_grades():

    clean_list = get_clean_data()

    grades = [
        { "name": m["name"], "marks": m["marks"], "grade":
          "A" if m['marks'] >= 90 else
          "B" if m['marks'] >= 75 else
          "C" if m['marks'] >= 60 else
          "D" if m['marks'] >= 40 else
          "F"}
          for m in clean_list

    ]

    print("\n---------------------- Students Grades ----------------------")
    print()
    for s in grades:

        print(f"Name : {s['name']}    |    Marks : {s['marks']}     |     Grades : {s['grade']} ")


def show_top_students():

    clean_list = get_clean_data()

    top = [t for t in clean_list  if t['marks'] >= 75]

    print("\n-------------- Toppers ------------------")
    print()

    for s in top:
        if s["marks"] >= 90:
            grade = "A"

        elif s['marks'] >= 75:
            grade = "B"

        else:
            grade= "C"

        print(f"Name : {s['name']}   |   Marks : {s['marks']}     | Grades : {grade} ")

def show_marks_statistics():

    clean_list = get_clean_data()

    if not clean_list:
        print("\nNo Students Available for Statistics.")
        return

    marks_list = [m['marks'] for m in clean_list]

    total_students = len(clean_list)
    total_marks = sum(marks_list)
    avg = total_marks / total_students
    highest = max(marks_list)
    lowest = min(marks_list)

    print("\n--------- Marks Statistics ------------ ")
    print(f"\nTotal Students     : {total_students}")
    print(f"Average Marks      : {avg}")
    print(f"Highest Marks      : {highest}")
    print(f"Lowest Marks       : {lowest}")
    print("--------------------------------------------")


while True:
     print("\n===== Smart Data cleaning & Analysis System =====")
     print()
     print("* Select an Option :")
     print("\n1. View Original Data")
     print("2. Clean student Data")
     print("3. Show Passing Students")
     print("4. Show Student Grades ")
     print("5. Show Top Students")
     print("6. Marks Statistics")
     print("7. Exit")


     try:
          option = int(input("\nEnter your Choice:"))

     except ValueError:
         print("Invalid Choice!!")
         continue


     if  option == 1:
         view_original_data()

     elif option == 2:
         clean_student_data()

     elif option == 3:
         show_passing_student()

     elif option == 4:
         show_grades()


     elif option == 5:
         show_top_students()


     elif option == 6:
         show_marks_statistics()

     elif option == 7:
         print("\n------- Program End ---------")
         break

     else:
         print("Invalid Choice!! Please enter 1-7")

