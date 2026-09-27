#Program 4: Handle IndexError
print("\nProgram 4: Handle IndexError")

try:

    numbers = [13 ,26 ,38 ,49 , 75 ,88 ,42]
    index_num = int(input("\nEnter index number:-" ))
    print(numbers[index_num])

except IndexError:
    print("Index Error")
    print("index is out of range")
