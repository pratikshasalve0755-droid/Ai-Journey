#Program 3:  Append_student_OOP.py
print("\nAppend_student_OOP.py")

import csv



class Student:
    def __init__(self,  name , roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def to_list(self):
        return [ self.name , self.roll_no , self.marks]

name = input("\nEnter Name: ")
try:
   roll_no = int(input("Enter Roll_no:"))
   marks = int(input("Enter Marks:"))
except ValueError:
     print("Invalid Input! Roll_no and Marks should be integers")


s5 = Student(name, roll_no , marks)

with open("student_report.csv" , "a" , newline = "") as file:
     writer = csv.writer(file)
     #next(writer)
     writer.writerow(s5.to_list())

     print("Student added successfully!")



















"""with open("student_report.csv" , "w" , newline="") as  file:
    writer = csv.writer(file)
    writer.writerow(['Name'  ,'Roll_No' , 'Marks'])"""
