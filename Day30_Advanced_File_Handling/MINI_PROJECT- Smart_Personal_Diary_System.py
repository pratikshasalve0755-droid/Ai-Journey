# Mini Project : Smart Personal Diary
print("\nMini Project : Smart_Personal_Diary_System")


import os
import datetime

FILENAME = "diary.txt"

def write_new_entry():
    entry_title = input("Title:").strip()

    if not entry_title.strip():
        print("Title is empty!")
        return

    description = input("Description:").strip()

    if not description.strip():
        print("Description is empty!")
        return

    date = str(datetime.date.today())

    time = datetime.datetime.now().strftime("%H:%M:%S")

    with open (FILENAME , "a" ) as file:
        #print("=====================================")
        file.write(f"Title : {entry_title}\n")
        file.write(f"Description : {description}\n")
        file.write(f"Date : {date}\n")
        file.write(f"Time : {time}\n")
        #file.write("-" * 50 + "\n")
        #print("=====================================")

    print("\nDiary Entry Saved Successfully!")

def view_all_entries():
    if not os.path.exists(FILENAME):
        print("File Doesn't Exists!")
        return

    with open (FILENAME, "r") as file:
        content = file.read()

        if content == "":
            print("Content is empty , please enter new one!")


        else:
            print("\n========== Personal Diary ==========")
            print(content)
            print("--------------------------------------")



def search_entry():
    if not os.path.exists(FILENAME):
        print("File Doesn't Exists!")
        return

    title = input("Title:").strip()

    if not title.strip():
        print("Title is empty!")
        return


    with open(FILENAME , "r", encoding="utf-8") as file:
        content = file.read()

    entries = content.split("-" * 50)

    found = False

    for entry in entries:
        if f"Title : {title}".lower() in entry.lower():
            print("\nEntry Found!\n")
            print(entry)
            found = True
            break

    if not found:
        print("Entry not found!")

def delete_all_entries():
    if not os.path.exists(FILENAME):
        print("File Doesn't Exists!")
        return

    choice = input("Are you sure? (Y/N): ").strip().lower()

    if choice == "y":
        with open(FILENAME , "w") as file:
           pass


        print("All diary entries deleted successfully!")


    elif choice == "n":
        print("Deletion Canceled!")

    else:
        print("Invalid Choice!")


while True:
    print("\n=== My Personal Diary ===")
    print("\nSelect an option:")
    print("\n1. Add New Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    try:
        choice = int(input("\nEnter Your Choice:"))

    except ValueError:
        print("Invalid Choice")
        continue

    if choice == 1:
        write_new_entry()

    elif choice == 2:
        view_all_entries()

    elif choice == 3:
       search_entry()

    elif choice == 4:
        delete_all_entries()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")
        """

with open(filename, "w", encoding="utf-8") as file:
    pass
"""








