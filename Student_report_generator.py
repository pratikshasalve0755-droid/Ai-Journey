print("----STUDENT REPORT----")

marks_list =[]
for i in range(1,6):
   mark = int(input("Enter marks")
    marks_list.append(mark)
print("\nmarks_list=",marks_list)
name = input("\nEnter student name:")

def total_marks(marks_list):
    total = 0
    for mark in marks_list:
         total += mark
    return total

def average_marks(marks_list):
    total = total_marks(marks_list)
    average = total / len(marks_list)
    return average

def grade(average):

    if average >= 80:
        return "A"
    elif average >= 50:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"

def display_report(name, marks_list, total, average, final_grade):
  print("\nName:",name)
  print("total:",total)
  print("Average:",average)
  print("final_grade:",final_grade)

total = total_marks(marks_list)
average = average_marks(marks_list)
final_grade = grade(average)

display_report(name, marks_list, total, average, final_grade)
