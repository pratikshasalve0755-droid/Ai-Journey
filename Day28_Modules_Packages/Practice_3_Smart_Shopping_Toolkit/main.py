from shopping_tools.cart import add_items , remove_items
from shopping_tools.discount import (apply_discount , final_price ,display_result)

original_price = 0
discount_amt = 0
result = 0

while True:
     print()
     print("---- Smart Shopping Toolkit ----")
     print("Select an Option:")
     print("1. Add Item")
     print("2. Remove Item ")
     print("3. Calculate Bill")
     print("4. Display Results")
     print("5. Exit")

     try:
        choice = int(input("\nEnter your choice:"))

     except ValueError:
        print("Please Enter valid Choice")
        continue

     if choice == 1:
        add_items()

     elif choice == 2:
        remove_items()

     elif choice ==3:

        original_price, discount_amt = apply_discount()
        result = final_price(original_price, discount_amt)
        print(f"\nFinal Salary : {result}")


     elif choice ==4:
         display_result( original_price, discount_amt, result )

     elif choice ==5:
         print("Exiting...")
         break

     else:
         print("Please Enter a valid Choice")
