#app 1:Input_validation (ValueError)


try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid age!")
    print("Invalid literal for int() ")
