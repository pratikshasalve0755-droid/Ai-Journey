# Mini app : Secure Wallet System
print("Mini app : Secure Wallet System ")

class Wallet:
    def __init__(self ,name , balance):
        self.name = name
        if balance >= 0:
            self.__balance = balance
        else:
            self.__balance = 0
            print("Balance can't be negative!")

    def add_money(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0!")
            return

        self.__balance += amount
        print(f"Money added! New Balance: {self.__balance}")

    def spend_money(self , amount):
        if amount <= 0 :
            print("Amount should  be positive!")

        elif amount > self.__balance:
            print("Insufficient Balance")
            return

        else:
            self.__balance -= amount
            print(f"Spent successfully! Remaining Balance: {self.__balance}")


    def check_balance(self):
        return self.__balance


if __name__ == '__main__':

       name = input("\nEnter Name:").strip()
       try:
          balance = float(input("Enter initial Balance:"))
       except ValueError:
           print("Balance should be numeric!")
           balance = 0

       person = Wallet(name , balance)

       while True:
              print(f"\n----- Welcome To {person.name} -----")
              print("Select option")
              print("1. Add Money")
              print("2. Spend Money")
              print("3. Check Balance")
              print("4. Exit")
              print("--------------------------------------")
              try:
                 choice = int(input("Enter your choice:"))
              except ValueError:
                 print("Invalid choice!")
                 continue

              if choice == 1:
                 try:
                     amount = float(input("Enter Amount:"))
                     person.add_money(amount)
                 except ValueError:
                     print("Amount should be numeric!")

              elif choice == 2:
                 try:
                     amount = float(input("Enter Amount:"))
                     person.spend_money(amount)
                 except ValueError:
                     print("Amount should be numeric!")

              elif choice == 3:
                  print(f"Balance: {person.check_balance()}")

              elif choice == 4:
                 print("Thank you for Visiting !")
                 break

              else:
                 print("Invalid Choice!")















