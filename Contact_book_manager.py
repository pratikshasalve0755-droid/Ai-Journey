# Mini Project:Contact Book Manager
print("Mini Project: Contact Book Manager")

contact_book = {}

while True:
    print("\n------Welcome to Contact Book ------")
    print(" ---update your phone book---")
    print("\nSelect Options: "
          "\n1.Add contact \n"
          "2.Update contact \n"
          "3.Delete contact \n"
          "4.View all contacts \n"
          "5.Search contact \n" 
          "6.Exit")

    choice = int(input("\nEnter your choice:- "))

    if choice == 1:                               #Add contact
        name = input("Enter your Name:")
        number = input("Enter your Number:")

        if name in contact_book :
            print(f"\nThe contact {name} already exists!")
        else:
            contact_book[name] = number
            print(f"The contact {name} has added successfully!")

    elif choice == 2:                              #Update contact
        name = input("Enter name to update:")

        if name in contact_book:
            new_number = input("enter number to update:")
            contact_book[name] = new_number
            print(f"\nThe contact {name} has been updated!")
        else:
            print("The contact doesn't exist!")

    elif choice == 3:                         #Delete contact
        name =input ("Enter name to delete:")

        if name in contact_book:
           contact_book.pop(name)
           print(f"\nThe contact {name} has deleted successfully!")
        else:
           print(f"The contact {name} doesnt exist!")

    elif choice == 4:                             #View/Display contact
        if contact_book:
           print("\n--- Contact List ---")
           for name ,number in contact_book.items():
               print(name ,":" , number)

        else:
            print("The contact book is empty!")

    elif choice == 5:                                #Search contact
        name = input("Enter name to search:")

        if name  in contact_book:
           print("\n--- Contact List ---")
           print(f"\nThe contact {name} has found!")
        else:
           print(f"the contact {name} not found!")
           print("add contact first")

    elif choice ==6:                                  #Exit
        print("Exit")
        print("-----Thanks for visiting!----- ")
        break

    else:
        print("Invalid choice!")


