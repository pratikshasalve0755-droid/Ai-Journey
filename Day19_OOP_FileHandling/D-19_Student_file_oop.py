
# Program 1: Student_file_OOP.py
print("\nProgram 1: Student_file_OOP")

import csv

class Student:
    def __init__(self,  name , roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def to_list(self):
        return [ self.name , self.roll_no , self.marks]



s1 = Student( "Akash" , 1 ,  76)

s2 = Student("Bhavana" , 2 , 85)

s3 = Student("Chetan" , 3 , 77)

s4 = Student("drishti", 4 , 69)


students = [s1 , s2 , s3 , s4 ]



with open("student_report.csv", "w" , newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "RollNo", "Marks"])
    for s in students:
        writer.writerow(s.to_list())

print("\nStudents Data saved successfully!")