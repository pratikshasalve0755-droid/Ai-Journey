# Mini app : Restaurant Order Management System
print(" Mini app: Restaurant Order Management System")

class Dish:
    def __init__(self, dish_name , dish_price):
        self.dish_name = dish_name
        self.dish_price = dish_price

    def display(self):
        print(f"{self.dish_name} : {self.dish_price}")


class Order:
    def __init__(self , customer_name):
        self.customer_name = customer_name
        self.dish_list = []

class RestaurantManager:
    def __init__(self):
        self.menu = []
        self.orders = []

    def add_dish(self):
        dish_name = input("Enter Dish Name:")
        if not dish_name:
            print("Dish Name required!")
            return

        try:
            dish_price = float(input("Enter Dish Price:"))
        except ValueError:
            print("Price should be a numeric value!")
            return

        d1 = Dish(dish_name , dish_price)
        self.menu.append(d1)
        print("Dish Added to Menu")


    def create_order(self):
         cus_name = input("Enter Customer Name:").strip()
         if not cus_name:
             print("Customer Name required!")
             return

         order = Order(cus_name)
         self.orders.append(order)
         print("Customer added to Order list!")

    def dish_to_order(self):
        cus_name = input("Enter Customer Name:").strip()

        selected_order = None
        for order in self.orders:
            if order.customer_name.lower() == cus_name.lower():
                selected_order = order
                break

        if not selected_order :
            print("Customer not found!")
            return
        if not self.menu:
            print("Menu is Empty!")
            return

        print("\n--- Menu ---")
        for dish in self.menu:
            dish.display()

        d_name = input("Enter Dish Name:")

        selected_dish = None
        for dish in self.menu:
            if dish.dish_name.lower() == d_name.lower():
                selected_dish = dish
                break

        if selected_dish is None:
           print("Dish not found!")
           return

        if not selected_dish:
            print("Dish not found!")
            return

        selected_order.dish_list.append(selected_dish)
        print("Dish added to order!")

    def view_all_orders(self):
        if not self.orders:
            print("No Orders found!")
            return

        print("\n--- Order ---")

        for order in  self.orders:
            print("Customer: ", order.customer_name)

            if not order.dish_list:
                print("No dishes added!")

            else:
                print("Dishes:")
                for dish in order.dish_list:
                    dish.display()

    def calculate_total(self):
        if not self.orders:
           print("No Orders found!")
           return

        for order in self.orders:
            total_bill = 0
            print(f"\nCustomer: {order.customer_name}")

            if not order.dish_list:
               print("No Dishes found!")
            else:
               print("--- Dishes ---")
               for dish in order.dish_list:
                   print(f"{dish.dish_name} : {dish.dish_price}")
                   total_bill += dish.dish_price

               print(f"Total Bill : {total_bill}")

    def main_menu(self):
        while True:
            print("\nSelect Option")
            print("1. Add Dish")
            print("2. Create Order")
            print("3. Add Dish to Order")
            print("4. View All Orders")
            print("5. Calculate Total Bill")
            print("6. Exit")
            print("--------------------------")
            try:
                choice = int(input("Enter Your Choice:"))
            except ValueError:
                print("Invalid Value!")
                continue

            if choice == 1:
                self.add_dish()

            elif choice == 2:
                self.create_order()

            elif choice == 3:
                self.dish_to_order()

            elif choice == 4:
                self.view_all_orders()

            elif choice == 5:
                self.calculate_total()

            elif choice == 6:
                print("Exit!")
                break
            else:
                print("Invalid Choice!")

manager = RestaurantManager()
manager.main_menu()











