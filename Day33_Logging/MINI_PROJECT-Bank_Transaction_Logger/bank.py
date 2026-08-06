# MINI-PROJECT : SMART BANK TRANSACTION LOGGER
print("\nMINI-PROJECT: SMART BANK TRANSACTION LOGGING")


import logging

logging.basicConfig(
    filename = "bank.log",
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filemode = "a",
    encoding = "utf-8"
)

logging.info("Program Started!")
class BankAccount:

     def __init__(self, account_holder , balance):
          self.account_holder = account_holder
          self.__balance = balance


     def deposit(self):
         try:
            amount = float(input("Enter Amount:"))

         except ValueError:
            print("Invalid Amount!")
            logging.error("Non-numeric Value!")
            return

         if amount <= 0:
             print("Invalid Amount")
             logging.error(f"Invalid Deposit Attempt: ₹{amount}")
             return

         self.__balance += amount
         print(f"₹{amount} Deposited Successfully!")
         logging.info(
             f"₹{amount} deposited successfully. Balance = ₹{self.__balance}"
         )


     def withdraw(self):
         try:
             withdraw_amount = float(input("Enter Amount: "))
         except ValueError:
             print("Invalid Amount")
             logging.error("Non-numeric amount entered.")
             return
         if withdraw_amount <= 0:
            print("Amount must be greater than zero.")
            logging.error("Invalid Withdrawal Amount")
            return

         if withdraw_amount > self.__balance:
            print("Insufficient Balance!")
            logging.warning(f"Withdrawal Failed: Requested ₹{withdraw_amount}, Available ₹{self.__balance}")
            return


         self.__balance -= withdraw_amount
         print(f"Withdrawn Amount is: ₹{self.__balance}")
         logging.info(
             f"₹{withdraw_amount} withdrawn successfully. Remaining Balance = ₹{self.__balance}"
         )

         print("Amount Withdrawn Successfully!")


     def check_balance(self):
         print(f"\nAccount Holder : {self.account_holder}")
         print(f"Current Balance : ₹{self.__balance}")
         logging.info(
             f"{self.account_holder} checked balance. Balance = ₹{self.__balance}"
         )

user1 = BankAccount("Pratiksha" ,1000)
logging.info("Bank Account Created")

while True:
       print("\n====== Smart Bank ======")
       print("\nSelect an Option:")
       print("\n1. Deposit")
       print("2. Withdraw")
       print("3. Check Balance")
       print("4. Exit ")

       try:
          option = int(input("Enter an Option:"))

       except ValueError:
          print("Invalid Option!")
          logging.warning("Invalid menu option selected.")
          continue

       if option == 4:
           print("\nExiting...")
           logging.info("Program Closed!")
           break

       if option == 1:
           user1.deposit()

       elif option == 2:
           user1.withdraw()

       elif option == 3:
           user1.check_balance()

       else:
           print("Invalid Option!")
           logging.info("Invalid Option!")

