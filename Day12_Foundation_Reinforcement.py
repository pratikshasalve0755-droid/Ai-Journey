#Program 1:Create a dictionary of 3 students and store name ,age and marks
print("Program 1: Create a dictionary of 3 students and store name, age and marks")

students =[]
n = int(input("Enter number of students:-"))

for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))
    student = {'Name' : name , 'Age' : age, 'Marks' :marks}
    students.append(student)
    print("----------------------")

for student in students:
    for key, value in student.items():

        print(key , ":" ,value)

for student in students:
    print(f"student =    Name: {student['Name']} | Age: {student['Age']} | Marks:{student['Marks']}")

print("---------------------------------------------------------------------")

#Program 2:Create a dictionary of 5 user calculate total and average using functions
print("Program 2:Create a dictionary of 5 user  calculate total and average marks")

numbers = []

for i in range(5):
    num = int(input("Enter numbers:-"))
    numbers.append(num)

print("Numbers = ",numbers)

def total_average(nums):
    total = 0
    for num in nums:
        total  += num
    average = total / len(nums)
    return {"Total" : total , "Average" : average}

result = total_average(numbers)

print("Total:" , result["Total"])
print("Average:" ,result["Average"])

print("---------------------------------------------------------------------------")

#Program 3: Count frequency of each word using dictionary
print("Program 3: Count frequency of each word using dictionary")


freq ={}

for i in range(1):
    words = input("Enter sentences : ").lower().split()

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] =1

for key ,value in freq.items():
    print(key , ":" ,value)








