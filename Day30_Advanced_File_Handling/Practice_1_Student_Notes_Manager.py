#Program 1: Student Notes Manager
print("Program 1: Student Notes Manager")

import os

filename = "student_notes.txt"

if os.path.exists(filename):
    print("Student Notes Manager: File Exists")

else:
    print("Student Notes Manager: File Does Not Exists")

def add_note():
   note = input("Enter Your Note:")
   with open( filename, "at") as file:
        file.write("Daily Notes:-\n")
        print()
        file.write(f"* {note} *\n")
        print("Note Added Successfully! ")


def view_notes():
    if not os.path.exists(filename):
        print("No notes found!")
        return

    with open(filename, "r") as file:
        content = file.read()

    if content.strip() == "":
        print("No notes available!")
    else:
        print("\n-------- Student Notes --------")
        print(content)

def delete_all_notes():
    if not os.path.exists(filename):
        print("No notes to delete!")
        return

    choice = input("Are you sure you want to delete all notes? (Y/N): ").strip().lower()

    if choice == "y":
        with open(filename, "w", encoding="utf-8") as file:
            pass

        print("All notes deleted successfully!")

    elif choice == "n":
        print("Deletion Cancelled.")

    else:
        print("Invalid Choice!")

while True:
    print("\n=== Student Notes Manager ===")
    print("\nSelect an choice:")
    print("\n1. Add Notes")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Exit")
    try:
        choice =int(input("\nEnter Your Choice:"))

    except ValueError:
        print("Invalid Choice")
        continue

    if choice == 1:
        add_note()

    elif choice == 2:
        view_notes()

    elif choice == 3:
        delete_all_notes()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")


