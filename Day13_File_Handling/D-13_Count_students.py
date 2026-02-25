#Program 3:Count how many students are stored in file.
print("Program 3: Count how many students are stored in file.")

with open("Students.txt" ) as file:
    print(file.readlines())