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
