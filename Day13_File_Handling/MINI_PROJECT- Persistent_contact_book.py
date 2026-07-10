#Mini app : Persistent Contact Book
print("Mint app: Persistent Contact Book")

while True:
    print("-----Welcome to Contacts Book-----")
    print("Select Options :-\n"
          "1) Add contacts \n"
          "2) View contacts list\n"
          "3) Search contacts\n"
          "4) Exit")


    choice = int(input("Enter your choice:- "))

    if choice == 1:                                   #Add contacts
        name = input("Enter name :- " )
        number = input("Enter number :-")

        try:
            with open("Contacts.txt" , "a") as file:
                file.write(f"{name} : {number}\n")
            print("Data saved successfully!")

        except Exception as e:
            print("Error Occurred " ,e)

    elif choice == 2:                                  #View all contacts
        with open("Contacts.txt", "r") as file:
            for x in file:
                print(x)

    elif choice == 3:                      #search contacts
        name = input("Enter name  to search :-")
        found = False
        try:
            with open("Contacts.txt", "r") as file:
                for line in file:
                    if name in line.lower():
                        print(f"{name} found!")
                        print(line.strip())
                        found = True
            if not found:
                print("Contact not found!")
        except FileNotFoundError:
            print("No contacts file found!")


    elif choice == 4:            #Exit
        print("Exiting the Program!")
        break

    else:
        print("Error! , Invalid choice! Please try again.")
