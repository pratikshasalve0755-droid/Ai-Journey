# Mini app : Contact Book in OOP version
print("\nMini app: Contact Book  in OOP version")

class Contact:
    def __init__(self, name, phone ,email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print("----------------------------")
        print("Name:" , self.name)
        print("PhoneNo: " , self.phone)
        print("Email:" , self.email)
        print("----------------------------")

class ContactManager:
    def __init__(self):
        self.contacts_list = []

    def add_contact(self, name, phone, email):
        if not name or not phone or not email:
            print("All fields are required!")
            return

        if not phone.isdigit():
            print("Phone must contain only digits!")
            return

        if "@" not in email:
            print("Invalid email format!")
            return

        for contact in self.contacts_list:
            if contact.name.lower() == name.lower():
                print("Contact already exists!")
                return

        new_contact = Contact( name, phone ,email)
        self.contacts_list.append(new_contact)
        print(f"{name} added successfully!")

    def view_all_contacts(self):
        if not self.contacts_list:
            print("No contacts found!")
            return

        print("------- Contact List --------")
        for contact in self.contacts_list:
            contact.display()

    def search_contact(self,name):
        found = False

        for contact in self.contacts_list:
            if name.lower() in contact.name.lower():
                contact.display()
                found = True

        if not found:
                print(f"The {name} not found!")

    def delete_contact(self,name):
        found = False

        for contact in self.contacts_list:
            if contact.name.lower() == name.lower():
                self.contacts_list.remove(contact)
                print(f"The {contact.name} deleted successfully!")
                found = True
                break

        if not found:
                print("The contact not found!")


    def update_contact(self, name):
        found = False

        for contact in self.contacts_list:
            if contact.name.lower() == name.lower():
                print("Enter new details:")

                new_phone = input("New Phone: ").strip()
                new_email = input("New Email: ").strip()

                if new_phone:
                    if new_phone.isdigit():
                        contact.phone = new_phone
                    else:
                        print("Invalid phone! Keeping old value.")

                if new_email:
                    if "@" in new_email:
                        contact.email = new_email
                    else:
                        print("Invalid email! Keeping old value.")

                print("Contact updated successfully!")
                contact.display()
                found = True
                break

            if not found:
                print("Contact not found!")



contact_book = ContactManager()

while True:

    print("\n--------Contact Book ---------")
    print("\n1. Add contact\n"
          "2. View all contacts\n"
          "3. Search contacts\n"
          "4. Delete contact\n"
          "5. Update contact\n"
          "6. Exit" )
    print("--------------------------")

    try:
        choice = int(input("\nEnter your choice:"))
    except ValueError:
        print("Enter Valid choice!")
        continue

    if choice == 1:
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number:").strip()
        email = input("Enter Email Address:").strip()
        contact_book.add_contact(name, phone,email)

    elif choice == 2:
        contact_book.view_all_contacts()

    elif choice == 3:
        name = input("Enter Name to search:").strip()
        contact_book.search_contact(name)

    elif choice == 4:
        name = input("Enter name to delete:").strip()
        contact_book.delete_contact(name)

    elif choice == 5:
        name = input("Enter name to update: ").strip()
        contact_book.update_contact(name)

    elif choice == 6:
        print("The Program Exits! Thanks for Visiting!")
        break

    else:
        print("Enter Valid choice!, please select from 1-6.")












