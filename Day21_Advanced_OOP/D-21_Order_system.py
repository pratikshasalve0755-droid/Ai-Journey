# Program 3: Order_System.py
print("Program 3: Order_System.py")

class Item:
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"Product Name : {self.name}")
        print(f"Price : ₹{self.price}")
        print(f"Quantity : {self.quantity}")
        print(f"Total : ₹{self.price * self.quantity}")

class Order:
    def __init__(self):
        self.cart = []

    def add_item(self):
        name = input("Enter Item Name:").strip()
        if not name :
            print("Name id required!")
        try:
           price = float(input("Enter Item Price:"))
           quantity = int(input("Enter Quantity: "))
        except ValueError:
            print("The price and Quantity should be numeric!")
            return

        item1 = Item(name , price , quantity )
        self.cart.append(item1)

        print("Item added successfully!")


    def view_order(self):

         if not self.cart:
            print("No items in cart!")

         else:

            print("\n------ Product List ------")
            for item in  self.cart:
                item.display()
                print("----------------------")


    def calculate_total(self):
        total = 0
        for item in self.cart:
            total += item.price * item.quantity
        print("Total Price :" ,total)

    def main_menu(self):
        while True:
            print("\nSelect Option:")
            print("1. Add Item ")
            print("2. View Order ")
            print("3. Calculate Total")
            print("4. Exit")
            print("--------------------")
            try:
                choice = int(input("Enter Your Choice:"))
            except ValueError:
                print("Invalid Value!")
                continue

            if choice == 1:
                self.add_item()

            elif choice == 2:
                self.view_order()

            elif choice == 3:
                self.calculate_total()

            elif choice == 4:
                print("Exit!")
                break
            else:
                print("Invalid Choice!")


manager = Order()
manager.main_menu()




















