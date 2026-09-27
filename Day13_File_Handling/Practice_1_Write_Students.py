#Program 1: Write a Program in a file
print("Program 1: Write a Program in a file")

name = input("\nEnter name:-")
try:
    age = int(input("Enter age:-"))

    with open("Students.txt" , "a") as file:
        file.write(f"Name: {name} , Age: {age}\n" )
        print("Data saved successfully!")

except ValueError:
    print("Please Enter valid number for Age! ")
