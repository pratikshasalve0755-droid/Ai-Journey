# Mini app 1: Movie Collection Manger
print("Mini app 1:Movie Collection Manager")

movies_list = []

def add_movie():
    while True:

       title = input("\nMovie Title:-").lower()
       if  title:
           break

       else:
           print("Movie title can't be empty1\n Please enter title ")

    genre = input("Movie Genre:- ")

    while True:
        try:
          rating = float(input("Movie Rating:-"))
          if 0 <= rating <= 10:
              break
          else:
             print("Rating must be between 0 and 10.")

        except ValueError:
           print("enter valid rating!")

    movie = {'Title': title , 'genre' : genre  , 'Rating' : rating }
    movies_list.append(movie)

    print("Movie Added Successfully!")

def view_movies():
    if movies_list:
        print("\n------ Movies List ------")
        for movie in movies_list:
            for key, value in movie.items():
                print(f" {key}: {value}")
    else:
        print("No Movies in list")


def Search_movies():
    if not movies_list:
        print("No movies in the list.")
        return

    title = input("\nEnter movie title to search:-").lower()
    found = False

    for movie in movies_list:
        if movie["Title"].lower() == title.lower(): # case-insensitive ma
            print(f"\n{title} movie found!")
            for key , value in movie.items():
                print(key , ":" , value)
                found = True
                break

    if not found:
        print(f"{title} movie not found!")

def remove_movie():
    if not movies_list:
        print("No movies in the list.")
        return

    title = input("\nEnter movie title to remove:- ").lower()
    found = False

    for movie in movies_list:
        if movie["Title"].lower() == title:
            movies_list.remove(movie)
            print(f"{title} Movie removed successfully!")
            found = True
            break

    if not found:
        print("Movie not found.")

def main_menu():
    while True:
          print("\n------ Welcome to Movie Collection Manager ------")
          print("\nChoose Options :-")
          print("1) Add Movie:- \n"
                "2) View Movies:-\n"
                "3) Find Movie:- \n"
                "4) Remove Movie \n"
                "5) Exit")
          print("--------------------")


          try:
            choice = int(input("\nEnter your choice:-"))

          except ValueError:
               print("Enter valid choice!")
               continue

          if choice == 1:
               add_movie()

          elif choice == 2:
              view_movies()

          elif choice == 3:
              Search_movies()

          elif choice == 4:
             remove_movie()

          elif choice == 5:
              print("Thanks for using Movie Collection Manager!")
              break

          else:
              print("Invalid menu choice. Please select 1-5.")

main_menu()










