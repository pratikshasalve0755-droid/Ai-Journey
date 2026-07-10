# Mini app : Online Course Management System
print("Mini app : Online Course Management System")

class User:
    def __init__(self , name , email):
        self.name = name
        self.email = email

    def display_profile(self):
        print("\n--- Profile ---")
        print(f"Name : {self.name}")
        print(f"Email : {self.email}")


class Student(User):
    def __init__(self , name , email):
        super().__init__(name , email)
        self.course_enrolled = []

    def enroll_course(self , course):
        if not course.strip():
            print("Course can't be empty!")
            return

        if course in self.course_enrolled:
            print("Course already enrolled!")
            return

        self.course_enrolled.append(course)
        print(f"{course} Course Enrolled!")

    def view_course(self):
        if not self.course_enrolled:
            print("No course Enrolled!")
            return

        print("\nEnrolled Course:")
        for c in self.course_enrolled:
            print(f"-{c}")

        print("--------------------------------")

class Instructor(User):
    def __init__(self, name , email):
        super().__init__(name , email)
        self.courses_created = []

    def create_course(self, course):
        if not course.strip():
                print("Course name cannot be empty!")
                return

        if course in self.courses_created:
            print("Course already created!")
            return

        self.courses_created.append(course)
        print(f"{course} course Created successfully!")

    def view_courses(self):
        if not self.courses_created:
            print("No Course has created!")
            return

        print("\nCourse Created:")
        for c in self.courses_created:
            print(f"-{c}")

        print("--------------------------------")


print("\n----- Student Section ------")
student_name = input("\nEnter Student Name:")
student_email = input("Enter Student Email:")

student = Student(student_name , student_email)
student.display_profile()

while True :
    course = input("\nEnter Course Name:")
    if course.lower() == ".":
        break

    student.enroll_course(course)
student.view_course()

print("\n ----- Instructor Section ------ ")
instructor_name = input("Enter Instructor Name: ")
instructor_email = input("Enter Instructor Email:")

instructor = Instructor(instructor_name , instructor_email)
instructor.display_profile()

while True:
    course = input("Enter course Name:")
    if course.lower() == ".":
        break
    instructor.create_course(course)
instructor.view_courses()







