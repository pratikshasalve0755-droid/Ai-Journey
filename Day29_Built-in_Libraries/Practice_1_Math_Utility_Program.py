#Program 1: Math Utility Program

import math

while True:


    print("\n===== Math Utility Program =====")

    print("\nSelect Options")
    print("\n1. Square root"
          "\n2. Power of 2"
          "\n3. Factorial"
          "\n4. Ceil Value"
          "\n5. Floor Value"
          "\n6. Exit")
    try:
       option = int(input("\nEnter your choice:"))

    except ValueError:
        print("Invalid Option")
        continue

    if option == 6:
        print("Exit")
        break

    if option not in [1, 2, 3, 4, 5]:
        print("Invalid Option!")
        continue

    n = float(input("Enter a number:"))

    if option == 1:
        print("Square root: " , math.sqrt(n))

    elif option == 2:

        print("Power of 2: " , math.pow(n , 2))


    elif option == 3:
        if  n >= 0 and n.is_integer():
            print("Factorial :" , math.factorial(n))

        else:
            print("Factorial is only for non -negative integers")

    elif option == 4:
        if n % 1 == 0:
           print("Ceil Value:" , math.ceil(n))


    elif option == 5:
        print("Floor Value:" , math.floor(n))


    else:
        print("Invalid Option")

