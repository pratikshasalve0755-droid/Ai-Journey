# Mini app: Smart Employee Attendance System
print("\nMini app: Smart Employee Attendance System")

import datetime
import os
import statistics

attendee = []

while True:
    print()
    print("== == = Smart Employee Attendance System == == =")
    print("\n*Select Option")
    print("\n1. Mark Attendance ")
    print("2. View Attendance")
    print("3. Attendance Statistics")
    print("4. Show Current Directory")
    print("5. Exit")

    try:
        option = int(input("\nEnter Your choice:"))
        print()

    except ValueError:
        print("Invalid Option!")
        continue


    if option == 1:
        name = input("Enter Employee Name: ").strip()

        if not name:
            print("Employee name cannot be empty!")
            continue
        details = {

            "Emp_name": name ,

            'Date': str(datetime.date.today()),
            'Time': datetime.datetime.now().strftime("%H:%M:%S")
        }

        attendee.append(details)
        print("Attendance Marked!")

    elif option == 2:
        if not attendee:
            print("No Attendance Records!")
            continue

        print("\n====== Attendance Records ======")

        for record in attendee:
            print(f"\nEmployee Name : {record['Emp_name']}")
            print(f"Date          : {record['Date']}")
            print(f"Time          : {record['Time']}")
            print("-------------------------------")



    elif option == 3:
        if not attendee:
            print("No Attendance Records!")
            continue

        name_lengths = []

        for record in attendee:
            name_lengths.append(len(record["Emp_name"]))

        longest_name = max(attendee, key=lambda x: len(x["Emp_name"]))["Emp_name"]
        shortest_name = min(attendee, key=lambda x: len(x["Emp_name"]))["Emp_name"]

        print("\n===== Attendance Statistics =====")
        print(f"Total Employees       : {len(attendee)}")
        print(f"Average Name Length   : {statistics.mean(name_lengths):.2f}")
        print(f"Longest Name          : {longest_name}")
        print(f"Shortest Name         : {shortest_name}")
        print(f"First Employee        : {attendee[0]['Emp_name']}")
        print(f"Last Employee         : {attendee[-1]['Emp_name']}")

    elif option == 4:
        print(f"Current Working Directory: ")
        print(os.getcwd())

    elif option == 5:
        print("Thanks For visiting!")
        break

    else:
        print("Invalid Option!")






