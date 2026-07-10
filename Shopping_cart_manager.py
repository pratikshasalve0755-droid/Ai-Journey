#Mini app: Shopping Cart Manager
print("Mini app: Shopping Cart Manager")

print("\n---------Shopping Cart Manager----------")
cart = []
while True:

    choice =int(input("\nSelect options-\n"
                    "1. Add item\n" 
                    "2. Remove item\n"
                    "3. View cart\n"
                    "4. Show total items\n"
                    "5. Exit\n"
                    " \nEnter your choice:-"))
    print("-----------------------------------")
    if choice == 1:
        add_item =input("  Enter item:-")
        cart.append(add_item)
        print("  Cart:" ,cart)

    elif choice == 2:
        if  not cart:
            print("  The cart is empty!")
        else :
          remove_item = input("  Enter item:-")
          if remove_item in cart:
               cart.remove(remove_item)
               print(f"  {remove_item} item has removed")
               print("cart =",cart)
          else:
                print("  Item not in cart")

    elif choice == 3:
        if not  cart:
            print("   The cart is empty")
        else:
            print("Cart =", cart)

    elif choice ==4:
        total_items =len(cart)
        print(f"     The cart contains {total_items} items" )

    elif choice == 5:
        print("  The Program Exist . Thank you!")
        break

    else:
        print("  Enter valid choice!")
