# Program 1: student class with multiple objects
print("\nProgram 1: student class with  multiple objects")

class student:
    def __init__(self,name,rollNo , marks):
        self.name = name
        self.rollNo = rollNo
        self.marks = marks

    def display(self):
        print(self.name,"  |" , self.rollNo,"     |", self.marks)

print("\n")
print("Name" , "   |" ,    "Roll_No", "|" ,  "Marks")
print("------------------------------------------------")
s1 = student("Advik" , 21 , 78)
s2 = student("Rishi" , 22 , 86)
s3 = student("suraj" , 23 , 56)

s1.display()
s2.display()
s3.display()

