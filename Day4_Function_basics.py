# Program 1: Adding two numbers by using function

def add_numbers(a, b):
    return a + b
result= add_numbers (5, 7)
print("N1:", 5)
print("N2:", 7)
print("Sum:" , result )

print("----------------------------------------------------------------------------------------")

# Program 2: check_even_odd(num)


def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
       return  "Odd"
num = int(input(" Enter the number:"))
result = even_odd(num)
print("The number is :", result)


print("----------------------------------------------------------------------------------------")

#Program 3: Greet User

def greet_user(name):
    return "Hello! " + name

name = input("Enter your  name ")
print(greet_user(name))

print("----------------------------------------------------------------------------------------")

#Program 4: Calculate_area (radius)

def calculate_area (radius):
    pi = 3.14
    return pi * radius  * radius

radius = int(input(" Radius:"))
print(calculate_area(radius))

print("----------------------------------------------------------------------------------------")

#calculator_using_functions

def add(a, b):
    return a+ b

def subtract(a ,b):
    return a - b

def  multiply(a, b):
    return a * b

def divide (a , b):
    if b != 0:
        return a/b
    else:
        print("Error cannot divide by zero")

print("\nSelect the Option:",
      "\n1. Add ",
      "\n2. Subtract",
      "\n3. Multiply",
      "\n4. Divide")

while True:
    choice = int(input("\nEnter your choice:"))
    if choice == 5:
        break
    num1 = int(input("\nEnter num1 :"))
    num2 = int(input("Enter num2 :"))

    if choice == 1:
        print("Result:", add(num1 , num2))

    elif choice == 2:
        print("Result:", subtract(num1 , num2))

    elif choice == 3:
        print("Result:", multiply(num1 , num2))

    elif choice == 4:
        print("Result:", divide(num1 , num2))

    else :
        print("Invalid  choice")

print("----------------------------------------------------------------------------------------")







