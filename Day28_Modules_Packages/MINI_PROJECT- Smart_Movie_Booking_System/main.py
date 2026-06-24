from movies import add_movies, view_movies
from users import add_user, view_users
from booking import book_tickets


while True:

    print("\n===== Smart Movie Booking System =====")

    print("1. Add Movie")
    print("2. View Movies")
    print("3. Add User")
    print("4. View Users")
    print("5. Book Ticket")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Please enter numbers only!")
        continue

    if choice == 1:
        add_movies()

    elif choice == 2:
        view_movies()

    elif choice == 3:
        add_user()

    elif choice == 4:
        view_users()

    elif choice == 5:
        book_tickets()

    elif choice == 6:
        print("Thank you for using Smart Movie Booking System!")
        break

    else:
        print("Invalid choice!")