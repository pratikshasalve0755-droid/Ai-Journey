# Mini Project: Smart Employee Attendance System
print("\nMini Project: Smart Employee Attendance System")

import datetime
import os
#import statistics

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
        details = {

            'Emp_name': input("Enter Employee Name:").strip(),

            'Date': str(datetime.date.today()),
            'Time': datetime.datetime.now().strftime("%H:%M:%S")
        }
        attendee.append(details)
        print("Attendance Marked!")

    elif option == 2:
        print("== Attendance Records ==")
        if attendee:
            for record in attendee:
                print(f"\nEmployee name: {record['Emp_name']}")
                name = input("Enter Employee Name: ").strip()

                if not name:
                    print("Employee name cannot be empty!")
                    continue

                print(f"Date : {record['Date']}")
                print(f"Time : {record['Time']}")
                print("--------------------------")
        else:
            print("No Attendance Records!")

    elif option == 3:
        if not attendee:
            print("No Attendance Records!")
            break

        else:
            import statistics

            name_lengths = []

            for record in attendee:
                name_lengths.append(len(record["Emp_name"]))

            longest_name_len = max(attendee , key =lambda x: len(x["Emp_name"]))["Emp_name"]
            shortest_name_len = min(attendee, key = lambda x: len(x["Emp_name"]))["Emp_name"]

            print(" === Attendance Statistics ===")
            print(f"\nTotal Employees Marked: {len(attendee)}")
            print(f"Average Name Length: {statistics.mean(name_lengths):}")
            print(f"Longest Employee Name: {longest_name_len}")
            print(f"Shortest Employee Name: {shortest_name_len}")
            print(f"First Employee Name: {attendee[0]["Emp_name"]}")
            print(f"Last Employee Name: {attendee[-1]["EMp_name"]}")

    elif option == 4:
        print(f"Current Working Directory: \n {os.getcwd()}")

    elif option == 5:
        print("Thanks For visiting!")
        break

    else:
        print("Invalid Option!")






