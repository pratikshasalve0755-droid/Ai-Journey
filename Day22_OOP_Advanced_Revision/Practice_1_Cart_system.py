# Program 1: Product and Cart System
print("Program 1: Product and Cart System ")

class Product:
    def __init__(self , name , price ,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"Product Name : {self.name}")
        print(f"Product Price : {self.price}")
        print(f"Quantity : {self.quantity}")

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self):
        p_name = input("Enter Product Name:").strip()
        if not p_name:
            print("Product name is required!")

        try:
            p_price = float(input("Enter Product Price:"))
            p_quantity = int(input("Enter Quantity: "))
        except ValueError:
            print("price should be numeric!")
            print("Quantity should be integer!")

        product = Product(p_name , p_price , p_quantity)
        self.products.append(product)

        print("Product added successfully!")

    def view_product(self):
         if not self.products:
             print("No product in Cart!")

         print("------- Products List ------")
         for p in self.products:
             p.display()
         print("-------------------------")

    def calculate_total_price(self):
        total_price = 0
        for p in self.products:
                total_price += p.price * p.quantity
        print(f"Total Product Price : {total_price}")

    def main_menu(self):
        while True:
            print("\nSelect Option")
            print("1. Add Product")
            print("2. View Product")
            print("3. Calculate Total Price")
            print("4. Exit")
            print("--------------------------")
            try:
                choice = int(input("Enter Your Choice:"))
            except ValueError:
                print("Invalid Value!")
                continue

            if choice == 1:
                self.add_product()

            elif choice == 2:
                self.view_product()

            elif choice == 3:
                self.calculate_total_price()

            elif choice == 4:
                print("Exit!")
                break
            else:
                print("Invalid Choice!")

manager = Cart()
manager.main_menu()

