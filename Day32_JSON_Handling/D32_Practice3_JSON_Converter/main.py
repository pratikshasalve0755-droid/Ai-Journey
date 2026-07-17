# Program 3: JSON <-> Dictionary convertor
print("\nProgram 3: JSON <-> Dictionary")

import json


while True:
    print("\n===== JSON ↔ Dictionary Converter =====")
    print("\nSelect  an  Option:")
    print("\n1. Dictionary → JSON")
    print("2. JSON → Dictionary")
    print("3. Exit")

    try:
        option = int(input("\nChoose an Option:"))

    except ValueError:
        print("Invalid Choice")
        continue


    if option == 1:
        student = {
            "name": input("Enter Student Name:"),
            "age" : int(input("Enter Age:")),
            "course" : input("Enter Course Name:")
        }

        json_data = json.dumps(student)
        print("\nType Before Converting:",type(student))
        print(f"\nThe student dictionary convert to json string")
        print("\n", json_data)
        print("Type After Converting:" , type(json_data))


    elif option == 2:
        student ='{"name": "Shrutika Jadhav", "age": 21,"course": " AI & ML"}'


        stu_dict = json.loads(student)
        print("\nType :",type(student))

        print(f"\nThe student json string convert to python dictionary ")
        print("\n", stu_dict)
        print("Type After Converting:" , type(stu_dict))


    elif option == 3:
        print("Thanks for using this program")
        print("Exiting!!!!")
        break

    else:
        print("Invalid Option")