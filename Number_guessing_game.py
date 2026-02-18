# Number Guessing Game

import random
comp_choice = random.randint(1, 10)      # it generates the nuber between the 1  and 50

while True:

    user_choice = int(input("Enter the Number:"))
    if comp_choice > user_choice:
        print(" too low!")
    elif comp_choice < user_choice:
        print(" too high!")
    elif comp_choice == user_choice:
        print(" Right, you guess the number ")
        break
else:
    print(" invalid input")
