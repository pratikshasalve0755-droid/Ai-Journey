from users import users_list
from movies import movies_list

bookings = []


def book_tickets():

    if not users_list:
        print("No users registered!")
        return

    if not movies_list:
        print("No movies available!")
        return

    user_id = input("Enter User ID: ").strip()

    selected_user = None

    for user in users_list:
        if user["user_id"] == user_id:
            selected_user = user
            break

    if selected_user is None:
        print("User not found!")
        return

    movie_id = input("Enter Movie ID: ").strip()

    selected_movie = None

    for movie in movies_list:
        if movie["movie_id"] == movie_id:
            selected_movie = movie
            break

    if selected_movie is None:
        print("Movie not found!")
        return

    seats = int(input("Enter Number of Seats: "))

    if seats <= 0:
        print("Invalid seat count!")
        return

    if seats > selected_movie["available_seats"]:
        print("Not enough seats available!")
        return

    selected_movie["available_seats"] -= seats

    booking = {
        "booking_id": len(bookings) + 1,
        "user_name": selected_user["name"],
        "movie_name": selected_movie["name"],
        "seats": seats
    }

    bookings.append(booking)

    print("\n------ Ticket Booked Successfully -------")
    print(f"Booking ID : {booking['booking_id']}")
    print(f"User       : {booking['user_name']}")
    print(f"Movie      : {booking['movie_name']}")
    print(f"Seats      : {booking['seats']}")