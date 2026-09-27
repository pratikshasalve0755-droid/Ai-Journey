#Program 3: Student statistics
print("Program 3: Student Statistics")

import statistics

marks = [78, 85, 92, 67, 88 ,45]

while True:

    print("\n=== Student Statistics ===")
    print("\nSelect  Your Choice")
    print("\n1. Average Marks"
          "\n2. Median Marks"
          "\n3. Highest Marks"
          "\n4. Lowest Marks"
          "\n5. Exit ")

    try:
       option = int(input("\nEnter your choice:"))

    except ValueError:
        print("Invalid Option")
        continue

    if option == 5:
        print("Thank you! Exiting Student Statistics Program...")
        break

    if option not in [1, 2, 3, 4, 5]:
        print("Invalid Option!")
        continue


    if option == 1:
        print(f"\nMarks = {marks}")
        print(f"Average Marks: {statistics.mean(marks)}")

    elif option == 2:
        print(f"Marks = {marks}")
        print(f"Median Marks: {statistics.median(marks)}")

    elif option == 3:
        print(f"Marks = {marks}")
        print(f"Highest Marks: {max(marks)}")

    elif option == 4:
        print(f"Marks = {marks}")
        print(f"Lowest Marks: {min(marks)}")

    else:
        print("Invalid Option!")

