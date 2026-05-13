# Program 3: User Roles System
print("Program 3: User Roles System")


class User:
    def __init__(self , username):
        self.username = username

    def login(self):

        print(f"\nUsername: {self.username}")
        print("User Logged In!")

class Admin(User):
    def __init__(self , username):
        super().__init__(username)

    def delete_user(self, user_to_delete):
        print(f"{self.username} Admin has deleted user: {user_to_delete}!")

class Customer(User):
    def __init__(self , username):
        super().__init__(username)

    def purchase_item(self , item_name ):
        self.item_name = item_name
        print(f"{self.username} has purchased {self.item_name} item !")

A =  Admin("Pratiksha")
A.login()
A.delete_user("abc123")
C = Customer("Pratiksha ")
C.login()
C.purchase_item("Pizza")




