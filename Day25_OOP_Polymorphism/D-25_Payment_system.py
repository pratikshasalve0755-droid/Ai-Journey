# Program 2: Payment System
print("Program 2: Payment System")

class Payment:
    def pay(self):
        print("Payment can be done by using different !")

class UPI(Payment):
    def pay(self):
        print("Payment Done by using UPI!")

class Card(Payment):
    def pay(self):
        print("Payment done by using Card!")

class Cash(Payment):
    def pay(self):
        print("Payment done by using Cash!")


upi = UPI()
card = Card()
cash = Cash()

while True:

    print("\n---- Payment  System ----")
    print("\nSelect The Mode of the Payment!")

    print("1.UPI")
    print("2.Card")
    print("3.Cash")
    print("4.Exit")

    try:
        choice =  int(input("\nEnter Your Choice:"))
    except ValueError:
        print("Please Enter a choice!")
        continue

    if choice == 1:
        upi.pay()

    elif choice == 2:
        card.pay()

    elif choice == 3:
       cash.pay()

    elif choice == 4:
        print("Thanks for using!")
        break

    else:
        print("Invalid choice")






























