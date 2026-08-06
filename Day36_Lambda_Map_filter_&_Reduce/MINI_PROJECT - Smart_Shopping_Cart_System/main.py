#Mini-Project : Smart Shopping Cart System

print("\nMini-Project : Smart Shopping Cart System! ")

from functools import reduce

shopping_cart = []

def add_product():
    try:
        product_id = int(input("Enter Product ID: "))
    except ValueError:
        print("Invalid Product ID!")
        return

    for item in shopping_cart:
        if item["product_id"] == product_id:
            print("Product ID already exists!")
            return

    product_name = input("Enter Product Name: ").strip().title()
    if not product_name:
        print("Product name cannot be empty!")
        return

    try:
        price = float(input("Enter Price: "))
    except ValueError:
        print("Invalid Price!")
        return

    if price <= 0:
        print("Price must be greater than zero!")
        return

    category = input("Enter Category: ").strip().title()
    if not category:
        print("Category cannot be empty!")
        return

    products = {
        "product_id": product_id,
        "product_name": product_name,
        "price": price,
        "category": category
    }



    shopping_cart.append(products)
    print("\nProduct Added successfully!")

def view_products():
    if not shopping_cart:
        print("No Product found in cart!")
        return

    else:
        print("\n============== Shopping Cart =============")
        for item in shopping_cart:
            print("------------------------------------")
            print(f"\nProduct Id   : {item['product_id']}")
            print(f"Product Name   : {item['product_name']}")
            print(f"Price          : {item['price']}")
            print(f"Category       : {item['category']}")
        print("\n------------------------------------")

def discounted_products():
    if not shopping_cart:
        print("No Product found in cart!")
        return

    discounted_price  = list(map(lambda x: x['price'] * 0.90, shopping_cart))

    print("\n========= Discounted Products ==========")

    for i in range(len(shopping_cart)):
        print("-----------------------------------------------------------")
        print(f"Product Name     : {shopping_cart[i]['product_name']}")
        print(f"Original Price   : ₹{shopping_cart[i]['price']}")
        print(f"Discounted Price : ₹{discounted_price[i]}")
    print("---------------------------------------------------------------")

def premium_products():
    if not shopping_cart:
        print("No Product found in cart!")
        return

    premium = list(filter(lambda x : x['price'] > 1000 , shopping_cart))

    if not premium:
        print("No Premium Products Found!")
        return

    print("\n====== Premium Products ======")

    for p in premium:

        print(f"- {p['product_name']}   : (₹{p['price']:.2f})")
    print("\n--------------------------------------------")

def bill():
    if not shopping_cart:
        print("No Product found in cart!")
        return

    prices = [item['price'] for item in shopping_cart]

    total = reduce(lambda x, y: x + y, prices)

    discounted_total = reduce(lambda x, y: x + y, [p * 0.9 for p in prices])

    print("\n============ BILL ==============")
    print(f"\nTotal Amount     : {total}")
    print(f"Discounted Total   : {discounted_total}")
    print(f"Total Products     : {len(shopping_cart)}")
    print("\n================================")


while True:
    print("\nWelcome To Smart shopping Cart System!")
    print("\nSelect Option:")
    print("1. Add Product")
    print("2. View Products")
    print("3. Show Discounted Prices")
    print("4. Show Premium Products")
    print("5. Generate Final Bill")
    print("6. Exit")
    print()
    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Invalid Option")
        continue

    if option == 1:
        add_product()

    elif option == 2:
        view_products()

    elif option == 3:
        discounted_products()

    elif option == 4:
        premium_products()

    elif option == 5:
        bill()

    elif option == 6:
        print("==== Thank you for using Smart Shopping Cart System! ====")
        break

    else:
        print("Invalid Option!!")