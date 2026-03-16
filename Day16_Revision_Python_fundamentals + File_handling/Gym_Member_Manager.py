# Mini Project 2:Gym Member Manager
print("Mini Project 2: Gym Member Manager")

import csv
import os

FILE_NAME = "members.csv"
VALID_MEMBERSHIPS = ["Basic", "Premium", "VIP"]

# ---------- Ensure file exists ----------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Membership"])


#-------------ADD MEMBER---------
def add_member():

    name = input("Enter Name:-").lower()
    if name.strip() == "":
        print("Name cannot be empty!")
        return

    try:
        age = int(input("Enter Age:-"))
    except ValueError:
        print("Invalid Age!")
        return

    membership = input("Enter type of Membership:-").strip().capitalize()
    if membership not in VALID_MEMBERSHIPS:
        print("Invalid membership type!")
        print("Allowed types:", VALID_MEMBERSHIPS)
        return


    with open(FILE_NAME , "a" , newline="") as file:
        writer = csv.writer(file)

        writer.writerow([ name , age ,  membership ])

    print("Members  added succesfully!")


# ---------- VIEW Member ----------
def view_members():
    try:
        with open( FILE_NAME , "r" , newline="") as file:
            reader = csv.reader(file)
            next(reader , None)

            print(" Name  |   Age  |  Membership ")
            print("------------------------------------")

            for row in reader:
                if len(row) >= 3:
                   print(f"{row[0]:<7}| {row[1]:<6} | {row[2]}")

    except FileNotFoundError:
        print("Members file not found!")

# ---------- SEARCH Members ----------
def search_member():
    name = input("Enter name to search:- ").strip().lower()
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                if row[0].lower() == name:
                    print("\nMember Found:")
                    print(f"Name: {row[0]}")
                    print(f"Age: {row[1]}")
                    print(f"Membership: {row[2]}")
                    found = True
                    break

        if not found:
            print("Member not found!")

    except FileNotFoundError:
        print("Members file not found!")

# ---------- count total  Members ----------
def count_total_members():
    total_members = 0

    try:
        with open(FILE_NAME , "r" ) as file:
            reader = csv.reader(file)
            next(reader,None)

            for row in reader:
                total_members += 1

        print("Total members = ", total_members)

    except FileNotFoundError:
        print("Members File not found!")


# ---------- DELETE Members ----------
def delete_member():
    name = input("Enter name to delete:-")
    rows = []
    header = None
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0].lower() != name:
                    rows.append(row)
                else:
                    found = True

    except FileNotFoundError:
        print("Members file not found!")
        return
    if not found:
        print("Members not found in the file!")
        return

    with open ("members.csv" , "w" , newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    print("Members deleted successfully!")


# ---------- Update Member ----------
def update_member():

    name = input("Enter member name to update:- ").strip().lower()
    rows = []
    header = None
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                if row[0].lower() == name:

                    print("Member found. Enter new details.")

                    try:
                        new_age = int(input("Enter new age:- "))
                    except ValueError:
                        print("Invalid age!")
                        return

                    new_membership = input("Enter new membership (Basic/Premium/VIP):- ").strip().capitalize()

                    if new_membership not in VALID_MEMBERSHIPS:
                        print("Invalid membership type!")
                        return

                    rows.append([row[0], new_age, new_membership])
                    found = True

                else:
                    rows.append(row)

    except FileNotFoundError:
        print("Members file not found!")
        return

    if not found:
        print("Member not found!")
        return

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    print("Member updated successfully!")



def main_menu():
    while True:

          print("\n------- Welcome to Gym Member Manager-------- ")
          print("\nChoose options:- ")
          print("------------------------------------")

          print("\n1. Add Member  \n"
                  "2. View Members\n"
                  "3. Search Member\n"
                  "4. Count Total Members\n"
                  "5. Delete Member\n"
                  "6. Update Member\n"
                  "7. Exit ")
          print("--------------------")

          try:
             choice = int(input("\nEnter your choice:-"))

          except ValueError:
              print("Enter valid choice!")
              continue

          if choice == 1:
             add_member()

          elif choice == 2:
             view_members()

          elif choice == 3:
             search_member()

          elif choice == 4:
               count_total_members()

          elif choice == 5:
              delete_member()

          elif choice == 6:
              update_member()

          elif choice == 7:
               print("Thanks for using Gym Member Manager!")
               break

          else:
            print("Invalid menu choice. Please select 1-6.")

initialize_file()
main_menu()



