#Program 1: Create Dictionary for student
print("\nProgram 1: Create Dictionary for student")

"""students = []                                                 # initialize the list
n = int(input("Enter no of  students:"))

for _ in range(n):
    name = input("Enter name:")
    age = int(input("Enter age:"))
    marks = int(input("Enter marks:"))
    print("----------------------")
    student = {'name': name, 'age' : age, 'marks': marks}
    students.append(student)
print("----------------------")
total = 0
for each_student in students:
    total += each_student["marks"]
    print("\nTotal marks:" , total)

average =total / n
print("\nAverage marks: ", average)

for student in students:                              #loop through students list
  for key , value in student.items():
        print(key , ":", value)

  print("\n")"""
print("----------------------------------------------------------------------")

#Program 2: update marks in student dictionary and print updated dictionary
print("Program 2: Update marks in students Dictionary")

"""students = []                                         # initialize the list
n = int(input("\nEnter no of  students:"))

for _ in range(n):
    name = input("Enter name:")
    age = int(input("Enter age:"))
    marks = int(input("Enter marks:"))
    print("----------------------")
    student = {'name': name,'age': age , 'marks': marks}
    students.append(student)

for student in students:                             #display original data
    for key , value in student.items():
         print(   key , ":", value )
    print("----------------------")

for student in students:
    print("Updating marks for:", student["name"])
    new_marks = int(input("Enter new marks: "))
    student["marks"] = new_marks

for student in students:                                      #display updated data
   print(f"student = Name: {student['name']} | Age: {student['age']} | Marks:{student['marks']}")"""

print("-----------------------------------------------------------------------")

#Program 3:Count frequency of numbers using dictionary
print("Program 3:Count frequency of numbers using dictionary")

numbers = [1 ,2 ,2 ,3 ,1,4,2]
freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else :
        freq[num] = 1

for key , value in freq.items():
              print(key ,":" , value)
print("Frequency: " , freq)

print("-----------------------------------------------------------------------")
#Program 4: Create dictionary from user input (3 subjects + marks)
print("Program 4: Create dictionary from user input (3 subjects + marks)")

subjects = {}



for i in range(2):
    subject = input("Enter subject: ")
    marks = int(input("Enter marks:"))
    subjects[subject] = marks

    print("---------------------------")

highest = max(subjects.values())
smallest =min(subjects.values())

print("subjects:" ,subjects)
print("Highest: ", highest)
print("smallest:", smallest)
print("---------------------------")

for key ,value in subjects.items():
    print(key , ":" ,value)








