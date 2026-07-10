# Mini app : Movie_Collection_Manager.py
print("\nMini app : Movie/Drama_Collection_Manager.py")

import csv
import os

class Movie:
    def __init__(self, title , genre , rating , year):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.year = year

    def to_list(self):
        return [self.title, self.genre, self.rating , self.year]


class MovieManager:
    def __init__(self):
        self.file_name = "movies_drama.csv"

    def add_movie(self):

        title = input("\nEnter title:").strip()
        genre = input("Enter genre:").strip()

        if not title or not genre :
                print("Title , Genre cannot be empty!")
                return

        try:
            rating = float(input("Enter rating (0-10):"))
            year = int(input("Enter year : "))

        except  ValueError:
            print("Rating and Year must be numeric!")
            return

        if rating < 0 or rating > 10:
            print("Rating must be between 0 and 10!")
            return

        movie = Movie( title , genre , rating , year)

        file_exists = os.path.isfile(self.file_name)

        with open (self.file_name , "a" , newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
               writer.writerow(["Title" , "Genre" , "Rating" ,"Year"])

            writer.writerow(movie.to_list())

        print("Movie/Drama Added Successfully!")


    def view_movies(self):
        try:
            with open(self.file_name , "r" , newline="") as file:
                 reader = csv.reader(file)
                 next(reader , None)

                 found = False

                 print("     Title     |     Genre     |     Rating     |     Year     ")
                 print("----------------------------------------")

                 for row in reader:
                    print(f"     {row[0]}     |     {row[1]}     |     {row[2]}     |     {row[3]}     ")
                    found = True


                 if not found:
                   print("Movie/Drama not Found!")

        except FileNotFoundError:
            print("File not found!")


    def search_movie(self):
        title = input("Enter Title to search:")
        found = False

        try:
            with open(self.file_name , "r" , newline="") as file:
                reader = csv.reader(file)
                next(reader , None)


                for row in reader:
                    if title.lower() == row[0].lower():
                       print("\n----- Movie/Drama List ----")
                       print(f"Title : {row[0]}")
                       print(f"Genre : {row[1]}")
                       print(f"Rating : {row[2]}")
                       print(f"Year : {row[3]}")
                       print("\n Movie/Drama Found")

                    found = True
                    break

            if not found:
                print("Movie/Drama not found!")

        except FileNotFoundError:
            print("File Not Found!")


    def delete_movie(self):
        title = input("Enter title to delete:")
        rows = []
        header = None
        found = False

        try:
             with open(self.file_name , "r" , newline="") as file:
                 reader = csv.reader(file)
                 header = next(reader )

                 for row in reader:

                     if row[0].lower() != title.lower() :
                        rows.append(row)
                     else:
                        found = True

        except FileNotFoundError:
             print("Movie/Drama file not found!")
             return

        if not found:
            print("Movie/Drama not found in the file!")
            return

        with open(self.file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)

        print("Movie/Drama deleted successfully!")


    def average_rating(self):
        total = 0
        count = 0

        try:
            with open(self.file_name , "r" ,  newline = "") as file:
                 reader = csv.reader(file)
                 next(reader , None)

                 for row in reader:
                     rating = float(row[2])
                     total += rating
                     count += 1
                     continue

                 if count == 0:
                     print("No movies found!")
                 else:

                     avg_rating = total / count
                     print("Average Rating: " , avg_rating)


        except FileNotFoundError:
            print("File not found!")

    def main_menu(self):
        while True:

            print("---- \nWelcome To Movie Collection ----")
            print("\nSelect option")
            print("1. Add Movies/Dramas"
                "\n2. View Movies/Dramas"
                "\n3. Search Movie/Drama"
                "\n4. Delete Movie/Drama"
                "\n5. Average Ratings"
                "\n6. Exit")
            print("-------------------------")

            try:
                choice = int(input("\nEnter your choice: "))
            except ValueError:
                print("Invalid input!")
                continue

            if choice == 1:
                self.add_movie()

            elif choice == 2:
                self.view_movies()

            elif choice == 3:
                self.search_movie()

            elif choice == 4:
                self.delete_movie()

            elif choice == 5:
                self.average_rating()

            elif choice == 6:
                print("Thanks for visiting! ")
                break

            else:
                print("Invalid choice!")


manager = MovieManager()
manager.main_menu()

"""with open("movies_drama.csv" , "w" , newline="") as  file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Title' , 'Genre' ,'Rating' , 'Year'])"""























