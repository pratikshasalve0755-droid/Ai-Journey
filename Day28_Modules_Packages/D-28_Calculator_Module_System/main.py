from calculator import add, subtract, multiply, divide

while True:
    print()
    print("------- Calculator -------")

    print("\nSelect Option:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("\nEnter Your choice:"))
    if choice == 5:
        print("Exiting........")
        break
    if choice in [1,2,3,4]:

        num1 = int(input("Enter Num1:"))
        num2 = int(input("Enter Num2:"))

    if choice == 1:
        print(f"Addition:{num1} +{num2} = {add(num1,num2)}")

    elif choice == 2:
        print(f"Subtraction:{num1} - {num2} = {subtract(num1, num2)}")

    elif choice == 3:
        print(f"Multiplication: {num1} * {num2} = {multiply(num1 ,num2)}")

    elif choice == 4:
        try:

            print(f"Division: {num1} / {num2} = {divide(num1,num2)}")

        except ZeroDivisionError:
                print("Cant divide by zero!")

    else:
        print("Invalid Choice")






