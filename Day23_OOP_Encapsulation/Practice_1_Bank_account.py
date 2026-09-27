# Program 1 : Bank Account
print("Program 1: Bank Account")


class Account:
    def __init__(self , acc_holder , balance):
        self.acc_holder = acc_holder

        if balance >= 0:
           self.__balance = balance
        else:
           self.__balance = 0
           print("Balance can't be negative!")

    def deposit(self ,  d_amount):

            if d_amount > 0:
                self.__balance += d_amount
                print("Amount added to the account!")
            else:
                print("Amount must be positive!")


    def withdraw(self ,  w_amount):

        if w_amount <= 0:
            print("Amount must be Positive!")

        elif  w_amount > self.__balance :
            print("Insufficient balance!")

        else:
           self.__balance -= w_amount
           print(f"{w_amount} withdrawn .\n New Balance : {self.__balance}")


    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
        name = input("\nEnter your Name:").strip()
        my_account = Account(name , 0)  #object


        while True :
             print("\n----- Bank Menu -----")
             print("Select Option")
             print("1. Deposit Money")
             print("2. Withdraw Money")
             print("3. Check Balance")
             print("4. Exit")

             try:
                 choice  = int(input("Enter your choice :"))

             except ValueError:
                 print("Invalid Choice!")


             if choice == 1 :
                 try:
                  amount = float(input("Enter amount:"))
                  my_account.deposit(amount)
                 except ValueError :
                  print("The amount should be numeric")

             elif choice == 2 :
                 try:
                   amount = float(input("Enter amount:"))
                   my_account.withdraw(amount)
                 except ValueError:
                    print("The amount should be numeric")

             elif choice == 3 :
                 balance = my_account.get_balance()
                 print(f"\nBalance : {balance}")

             elif choice == 4:
                 print("Thank you for using this program!")
                 break

             else:
                 print("Invalid Choice!")






















