# Program 3: Passward  Protection
print("Program 3: Passward Protection")

class User:
    def __init__(self , username , password):
        self.username = username
        self.__password = password

        if not password:
            print("Password can't be empty!")
            self.__password = "default123"

        else:
            self.__password = password

    def check_password(self , password):

        if password == self.__password:
          print("Correct Password! 👍")

        else:
            print("Incorrect Password! 👎")


    def change_password(self ,  old_password , new_password):

        if old_password != self.__password:
            print("Incorrect Password")
            return

        if not new_password:
            print("Please Enter New password")
            return

        if len(new_password) < 5 :
            print("Password can't be less than 5 characters!")
            return

        if old_password == new_password:
            print("Old password  can't be same as New Password! ")
            return


        self.__password = new_password
        print("New Password set successfully!")


if __name__ == "__main__":
    username  = input("\nEnter Username:")
    password = input("Enter Password:")

    user1 = User(username, password)

    check = input("\nEnter password to login: ")
    user1.check_password(check)


    choice = input("Do you want to change the Password (y/n) : ")
    if choice == 'y':
        old_password = input("Enter old password:")
        new_password = input("Enter new password:")
        user1.change_password(old_password  , new_password)





