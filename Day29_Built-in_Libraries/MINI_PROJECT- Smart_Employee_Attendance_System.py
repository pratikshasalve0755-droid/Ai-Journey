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

    if option == 5:
        print("Thanks For visiting!")
        break

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
                print(f"Date : {record['Date']}")
                print(f"Time : {record['Time']}")
                print("--------------------------")
        else:
            print("No Attendance Records!")

    elif option == 3:
        print(f"Total Employees Marked: {len(attendee)}")

    elif option == 4:
        print(f"Current Working Directory: \n {os.getcwd()}")







