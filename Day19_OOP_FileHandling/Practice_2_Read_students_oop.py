# Program 2: Read_student_oop.py
print("Program 2: read_student_oop.py")

import csv


class Student:
    def __init__(self,  name , roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("----------------------")
        print("Name: ",self.name)
        print("Roll_no: " , self.roll_no)
        print("Marks: ",  self.marks)


students = []

with open ("student_report.csv" , "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name = row[0]
        roll_no = int(row[1])
        marks = int(row[2])

        s = Student(name , roll_no , marks)
        students.append(s)

for s in students:
    s.display()

