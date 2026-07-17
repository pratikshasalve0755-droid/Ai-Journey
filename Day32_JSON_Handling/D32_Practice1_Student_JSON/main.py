# Project 1: Student JSON creator
print("\nProject 1: Student JSON Creator")



import json

FILENAME= "student.json"



student = {
    "name": input("\nEnter Name:"),
    "age": int(input("Enter Age:")),
    "course": input("Enter Course:"),

    "skills" : []
}

skills_input = input("Enter Skills (comma separated):")
student["skills"] = skills_input.split(",")


with open(FILENAME , "w") as file:
    json.dump(student, file , indent =4)

    print(f"\nStudent data saved to {FILENAME}")


print("=== Students Data === ")
with open (FILENAME , "r" )as file:
    data = json.load(file)


    print("\nName:", data["name"])
    print("\nAge: ",data["age"])
    print("\nCourse :", data["course"])
    print("\nSkills : ", " , " .join(data["skills"]))