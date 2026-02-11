#Program 1: Create Tuple print first , second value  , length  and try changing value(errror)
print("Program 1: Create Tuple print first , second value  , length  and try changing value(errror)")

coordinates = ( 12, 45, 78 , 98 ,56 )
print("\nCoordinates =",coordinates)

print("\nThe first value in tuple is: " ,coordinates[0])     #print the value at index 0
print("The second value in tuple is: " ,coordinates[1])     #print the value at index 1

print("------------------------------------------------------------------------------------")

#Program 2: Create a Dictionary ( Print name ,Add "grade",Update marks;Remove age,
# Print all keys,Print all values
print("Program 2: Create a Dictionary ( Print name ,Add (grade),Update marks,"
      "Remove age,Print all keys,Print all values")

print("\n")
student ={ "name" : "niki",
           "age": 25,
           "marks": 88}

print("student =" ,student)             #print entire dictionary
a=student["name"]
print("\n1. The value of the  name key :" ,a)                        #print value of the name key

student.update({"marks" : 78})
print("\n2. Updated dictionary= " ,student)                            #updates the marks

student.pop("age")
print("\n3. The  deleted key =", student)                              # removes the age key

x = student.keys()
print("\n4. The keys =", x)                                            # prints all keys

y = student.values()
print("\n5. The values =", y)