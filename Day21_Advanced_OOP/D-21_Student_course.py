#Program 2: Student + Course Mapping
print("\nProgram 2: Student + Course Mapping")


class Student:
    def __init__(self, name):
        self.name = name
        self.course_list = []

    def add_course(self , course):
        self.course_list.append(course)

    def display(self):
        print(f"Student Name: {self.name}" )
        if not  self.course_list:
            print("No courses assigned!")

        else:
            print(f"Courses :")
            for c in self.course_list:
                print("-" , c)

"""class Course:
    def __init__(self , course):
        self.course = course"""


class StudentManager:
    def __init__(self):
        self.student_list = {}

    def add_student(self):
        name = input("Enter name :").strip()

        if name in self.student_list:
            print("student already exist!")
        else:

            self.student_list[name] = Student(name)
            print("Student added successfully!")

    def assign_course(self):
        name = input("Enter Name: ").strip()

        if name not in self.student_list:
            print("Student not found!")
            return

        course = input("Enter Course: ").strip()
        self.student_list[name].add_course(course)
        print("Course assigned successfully!")


    def view_students(self):
        #name = input("Enter  name:")
        if not self.student_list:
            print(" No student Found!")
            return

        print("\n------Students List ---------")
        for student in self.student_list.values():
            student.display()

    def main_menu(self):
        while True:
            print("\nSelect Option:")
            print("1. Add Student ")
            print("2. Assign Courses ")
            print("3. View Students")
            print("3. Exit")
            print("--------------------")
            try:
                choice =  int(input("Enter Your Choice:"))
            except ValueError:
                print("Invalid Value!")
                continue

            if choice == 1:
                    self.add_student()

            elif choice == 2:
                self.assign_course()

            elif choice == 3:
                    self.view_students()

            elif choice == 3:
                    print("Exit!")
                    break

            else:
                    print("Invalid Choice!")


manager = StudentManager()
manager.main_menu()

        

        





















































































































