# Mini Project 2: Student Marks Analyzer

marks = []

num = int(input("\nEnter number of students:"))
for  i in range (num):
    mark =int(input("Enter marks:"))
    marks.append(mark)

print("\nMarks =" , marks)

total_marks=sum(marks)
print("\nTotal marks:" , total_marks)
average_marks = total_marks/num
print("Average marks: " , average_marks)
print("Highest_marks:" , max(marks))
print("Lowest marks:" ,min(marks))
