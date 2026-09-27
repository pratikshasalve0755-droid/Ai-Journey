# Program 3: feedback_collection_system
print("Program 3: feedback collection system")


import os
import datetime

filename = "feedback.txt"

if os.path.exists(filename):
    print("feedback.txt file exists")

else:
    print("feedback.txt file does not exist")


def add_feedback():

    name = input("Enter Your Name:").strip()

    if name == "" :
        print("Please enter name , name can't be blank")


    try:
        rating = int(input("Enter Rating (1-5):"))

    except ValueError:
        print("Please enter a valid number")

    if rating > 5 or rating < 1:
        print("Rating must be between 1 and 5!")


    comment = input("Enter Comment: ").strip()

    if comment == " " :
        print("Please enter comment , comment can't be blank")

    date = str(datetime.date.today())


    with open(filename , "a" , encoding="utf-8") as file:
        #file.write(f"    {name}    |    {rating}    |    {comment}    |    {date} \n")
        file.write(f"{name} | {rating} | {comment} | {date}\n")
    print("FeedBack Added Successfully!")



def view_feedback():
    if not os.path.exists(filename):
        print("feedback.txt file does not exist")
        return

    with open(filename , "r") as file:
        fb = file.read()

    if fb.strip() == " ":
        print("Please enter feedback , feedback can't be blank")


    else:
        print("\n----------------- FeedBack List ----------------")
        print(fb)
        print("------------------------------------------------")


def show_avg_rating():
    if not os.path.exists(filename):
        print("feedback.txt file does not exist")
        return

    ratings = []

    with open(filename , "r") as file:
        for line in file:
            name, rating, comment, date = line.strip().split("|")

            rating = int(rating.strip())
            ratings.append(rating)

    if len(ratings) == 0:
        print("No feedback available!")
        return

    total = 0

    for r in ratings:
         total += r

    avg_ratings = total / len(ratings)

    print(f"\nAverage Rating : {avg_ratings:.2f}")


while True:
    print("\n=== FeedBack Collection System ===")
    print("\nSelect an choice:")
    print("\n1. Add Feedback")
    print("2. View Feedback")
    print("3. Show average Rating")
    print("4. Exit")
    try:
        choice =int(input("\nEnter Your Choice:"))

    except ValueError:
        print("Invalid Choice")
        continue

    if choice == 1:
        add_feedback()

    elif choice == 2:
        view_feedback()

    elif choice == 3:
       show_avg_rating()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")
        """

with open(filename, "w", encoding="utf-8") as file:
    pass
"""
