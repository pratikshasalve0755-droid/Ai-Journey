# Program 3: Bank Account System

print("Program 3: Bank Account System")

class Account:
    def __init__(self, name , balance):
        self.name = name
        self.balance = balance

    def display(self):

        print(f"\nAccount holder name : {self.name}")
        print(f"Balance : {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = []

    def find_account(self, name):
        for acc in self.accounts:
            if acc.name.lower() == name.lower():
                return acc
        return None

    def create_account(self):
        name = input("Enter Account holder name:").strip()
        if not name:
            print("Name is required!")
            return

        try:
           balance = float(input("Enter Initial Balance:"))
        except ValueError:
            print("Balance should be numerical value!")
            return

        if balance < 0 :
            print("Amount  must be positive!")
            return

        account1 = Account(name, balance)
        self.accounts.append(account1)
        print("Account created successfully!")

    def deposit_money(self):
        name = input("Enter Account holder name:").strip()
        if not name:
            print("Name is required!")
            return

        acc = self.find_account(name)

        if acc is None:
            print("Account not found!")
            return

        try:
           deposit_amount = float(input("Enter amount to deposit:"))
        except ValueError:
            print("Amount should be numerical value!")
            return

        if deposit_amount <= 0 :
            print("Amount  must be positive!")
            return

        print("----------------------------")
        print(f"Old Balance : {acc.balance}")
        acc.balance += deposit_amount
        print(f"Deposit Amount : {deposit_amount}")
        print(f"New Balance : {acc.balance}")

        print(f"\n₹{deposit_amount } Amount deposited successfully!")


    def withdraw_money(self):
        name = input("Enter Account holder name:").strip()
        if not name:
            print("Name is required!")
            return

        acc = self.find_account(name)

        if acc is None:
            print("Account not found!")
            return

        try:
           withdraw_amount = float(input("Enter amount to Withdraw:"))
        except ValueError:
            print("Amount should be numerical value!")
            return

        if withdraw_amount <= 0 :
            print("Amount  must be positive!")
            return

        print("----------------------------")
        print(f"Old Balance : {acc.balance}")
        acc.balance -= withdraw_amount
        print(f"Deposit Amount : {withdraw_amount}")
        print(f"New Balance : {acc.balance}")

        print(f"\n₹{withdraw_amount} Amount withdrawn successfully!")


    def view_balance(self):
        name = input("Enter Account holder name:").strip()
        acc = self.find_account(name)

        if acc is None:
            print("Account not found!")
            return

        acc.display()

    def main_menu(self):
        while True:
            print("\nSelect Option")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Balance")
            print("5. Exit")
            print("--------------------------")
            try:
                choice = int(input("Enter Your Choice:"))
            except ValueError:
                print("Invalid Value!")
                continue

            if choice == 1:
                self.create_account()

            elif choice == 2:
                self.deposit_money()

            elif choice == 3:
                self.withdraw_money()

            elif choice == 4:
                self.view_balance()

            elif choice == 5:
                print("Exit!")
                break
            else:
                print("Invalid Choice!")

manager = Bank()
manager.main_menu()




















