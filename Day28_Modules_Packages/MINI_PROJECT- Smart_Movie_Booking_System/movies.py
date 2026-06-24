movies_list = []


def add_movies():

    movie = {
        "movie_id": input("Enter Movie ID: ").strip(),
        "name": input("Enter Movie Name: ").strip(),
        "year": int(input("Enter Movie Year: ")),
        "language": input("Enter Language: ").strip(),
        "genre": input("Enter Genre: ").strip(),
        "duration": int(input("Enter Duration (mins): ")),
        "available_seats": int(input("Enter Available Seats: "))
    }

    movies_list.append(movie)

    print(f"Movie '{movie['name']}' added successfully!")


def view_movies():

    if not movies_list:
        print("No movies available!")
        return

    print("\n----- Available Movies -----")

    for movie in movies_list:

        print(
            f"\nMovie ID: {movie['movie_id']}"
            f"\nName: {movie['name']}"
            f"\nYear: {movie['year']}"
            f"\nLanguage: {movie['language']}"
            f"\nGenre: {movie['genre']}"
            f"\nDuration: {movie['duration']} mins"
            f"\nAvailable Seats: {movie['available_seats']}"
        )

        print("-------------------------")