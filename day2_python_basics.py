#Program 1: printing basic personal details

Name = "Pratiksha"       # the pratiksha name is asign to variable name

Age = 22                # the 22 age is asign to variable Age

Goal = "learn to Code"     # learn to code is asign to variable goal

print(Name, Age , Goal)    # output : Pratiksha  22  Learn to  Code
OR
print("Name:Rutuja Gaikwad")
print("Age: 22 ")
print("Goal: Learn to Code")

---------------------------------------------------------------------------------------------------------

#Program 2: Greetings

Name = input("Enter your Name:")     # value taken from the user using input(Pratiksha)
print( "Hello" ,Name )               #output: Hello  Pratiksha

---------------------------------------------------------------------------------------------------------

#Program 3:Simple Calculator with Basics operation(+ , - ,* , / , %)

a = int(input ("Enter no1:"))        # the no1 input taken from user in integer datatype ( 5)
b = int(input ("Enter no2:"))        # the no2 input taken from user in integer datatype (2)
        
print("Add:", a + b)                # Add: 7
print("Subtract:", a - b)           # Subtract:3
print("Multiply:", a * b)           # Multiply: 10
print("Division:", a / b)           # Division : 2.5
print("Mod:", a % b)                # Mod : 1

---------------------------------------------------------------------------------------------------------

# Program 4: Convert Celsius to  Farenheit 

Celsius = float(input("Enter  temperature in Celsius:"))
Fahrenheit = (Celsius * 9/5) + 32
print ("Fahrenheit: " , Fahrenheit )

#output:
Enter  temperature in Celsius:234
Fahrenheit:  453.2

---------------------------------------------------------------------------------------------------------

# Program 5: Check positive or negative
num = int(input("Enter a number: "))
if num >= 0:
    print("Positive number")
else:
    print("Negative number")

#output:
Enter a number: 23
Positive number
or
Enter a number: -54
Negative number

  

        
