# Program 2: Student Marks Control
print("Program 2: Student Marks Control")


class Student:
    def __init__ (self , name , marks):
        self.name = name
        if 0 <= marks <= 100:
            self.__marks = marks

        else:
            self.__marks = 0
            print("Please enter marks between 0 and 100")

    def set_marks(self , mark):

        if 0 <= mark <= 100:
            self.__marks += mark
            print("Marks Added!")

        else:
            print("\nMarks can't be negative and should be greater than 0 and less than equal to 100!")

    def get_marks(self):
        return self.__marks


if  __name__ == "__main__":

    name = input("\nEnter Student Name:")
    student_marks = Student(name , 0)

    stu_marks = float(input("Enter Marks:"))
    student_marks.set_marks(stu_marks)
    print(f"Marks : {student_marks.get_marks()}")
