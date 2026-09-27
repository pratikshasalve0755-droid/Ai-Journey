#Program 2: Write a program to Read all Data from Students.txt file
print("Program 2: Write a program to Read all Data from Students.txt file ")



with open("Students.txt" , "r") as file:
    print(file.read())
    print("The Data has been read!")



#with open("Students.txt" , "w") as file:
 # (file.write(""))

