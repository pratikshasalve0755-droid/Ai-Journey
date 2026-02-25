#Program 4: Search students in file
print("Program 4: Search students saved in file")

name = input("Enter name  to search :-")
found = False
try:
    with open("Students.txt" , "r") as file:
         for line in file:
             if name in line.lower():
                print(f"{name} found!")
                print(line.strip())
                found = True
                break
    if not found:
         print(f"{name} not found")

except FileNotFoundError:
    print("Error! , file 'Students.txt' is not found")
except Exception as e:
    print ("Error found!",e)