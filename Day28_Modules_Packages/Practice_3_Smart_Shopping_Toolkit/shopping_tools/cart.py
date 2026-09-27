cart = []

def add_items():
        item = input("Add items:").strip()
        if item == " " :
            print("Please enter the item. ")
        cart.append(item)
        print(f"Item {item}has added to cart!")
        print(f"Current Cart:{cart}!")

def remove_items():
        if not cart:
           print("No items in the Cart")
           return

        items = input("Item to Remove:")
        if items in cart:
           cart.remove(items)
           print(f"Item {items} removed from cart!" )

           print(f"Updated Cart : {cart}")
        else:
            print("Item not found in cart!")
