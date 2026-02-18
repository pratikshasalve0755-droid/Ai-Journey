# Mini Project : Student Record Manager

print("\nMini Project : Student Record Manager")
print("\n")
name = input("Enter name:")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

student = {
    "name": name,
    "age": age,
    "marks": marks
}

# Grade Calculation
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

# Add grade to dictionary
student["grade"] = grade

# Display Student Record
print("\nStudent Record:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Marks:", student["marks"])
print("Grade:", student["grade"])
