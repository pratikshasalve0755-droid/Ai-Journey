#app 2:Division_program (ZeroDivisionError)
print("\napp 2:Division_program (ZeroDivisionError)")

try:
    num1 = int(input("\nEnter first number: " ))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result :- " ,result)
except ValueError:
    print("\nPlease Enter a valid number!")
    print("num1 is invalid literal for the int()")

except ZeroDivisionError:
    print("\ncan't divide by zero ")


