students = []                                         # initialize the list
n = int(input("\nEnter no of  students:"))

for _ in range(n):
    name = input("Enter name:")
    age = int(input("Enter age:"))
    marks = int(input("Enter marks:"))
    print("----------------------")
    student = {'name': name,'age': age , 'marks': marks}
    students.append(student)

    for student in students:

        print(f"student = Name: {student['name']} | Age: {student['age']} | Marks:{student['marks']}")
