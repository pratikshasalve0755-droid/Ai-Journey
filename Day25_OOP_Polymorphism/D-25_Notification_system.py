# Program 3: Notification System
print("Notification System")

class Notification:
    def send_message(self):
        print("Every notification can send message!")

class Email(Notification):
    def send_message(self):
        print("Email sent successfully!")

class SMS(Notification):
    def send_message(self):
        print("SMS sent successfully!")

class Whatsapp(Notification):
    def send_message(self):
        print("Message delivered successfully!")


email = Email()
sms = SMS()
wapp = Whatsapp()

while True:

    print("\n---- Payment System ----")
    print("\nSelect The Mode of the Payment!")

    print("1.Email")
    print("2.SMS")
    print("3.Whatsapp")
    print("4.Exit")

    try:
        choice =  int(input("\nEnter Your Choice:"))
    except ValueError:
        print("Please Enter a choice!")
        continue

    if choice == 1:
        email.send_message()

    elif choice == 2:
        sms.send_message()

    elif choice == 3:
       wapp.send_message()

    elif choice == 4:
        print("Thanks for using!")
        break

    else:
        print("Invalid choice!")




