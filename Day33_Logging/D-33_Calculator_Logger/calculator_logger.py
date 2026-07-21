# Program 2: Calculator Logger
print("Program 2: Calculator Logger")


import logging


logging.basicConfig(
    level = logging.INFO,
    filename = "calculator.log",
    filemode = "w" ,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)


def add(num1 , num2):

    result = num1 + num2
    logging.info(f"Added : {num1} + {num2} = {result}")
    return result

def sub(num1 , num2):

    result = num1 - num2
    logging.info(f"Subtracted : {num1} - {num2} = {result} ")
    return result

def mul(num1 , num2):

    result = num1 * num2
    logging.info(f"Multiplication  : {num1} * {num2} = {result}")
    return result

def div(num1 , num2):

    if num2 == 0:
        logging.error(f"Attempted division by zero: {num1} / {num2}")
        print("Cannot divide by zero!")
        return None

    result =  num1 / num2
    logging.info(f"Division : {num1} / {num2} = {result}")
    return result

while True:
    print()
    print(" === Calculator ===")
    print("\nSelect an option:")
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice:"))

    except ValueError:
        logging.error("Invalid Choice , Please Try Again")
        print("Invalid Choice")
        continue

    if choice == 5:
       logging.info("Exiting the Program")
       print("Exiting....")
       break

    try:
       num1 = float(input("Enter Number 1:"))
       num2 = float(input("Enter Number 2:"))

    except ValueError:
        logging.error("Please enter valid numbers")
        print("Please enter valid numbers")
        continue

    if choice == 1:
        print(f"Result:  {add(num1, num2)}")

    elif choice == 2:
        print(f"Result:  {sub(num1, num2)}")


    elif choice == 3:
        print(f"Result:  {mul(num1, num2)}")


    elif choice == 4:
        result = div(num1, num2)
        if result is not None:
            print(f"Result: {result}")

    else:
        logging.error("Invalid Choice")
        print("Invalid Choice")


