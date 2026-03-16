#Program 2: Practice-Dictionary logic
print("Program 2: Practice-Dictionary logic")

products = []
n = int(input("\nEnter number of products:-"))

for _ in range(n):
    product_name = input("Enter Product Name:-")
    price = float(input("Enter Price:-"))
    quantity = int(input("Enter Quantity:-"))
    print("----------------------------------")
    product = {'Product Name' : product_name , 'Price': price , 'Quantity': quantity }
    products.append(product)
    print("---------List of Products-------------------------")
    print(f"\nProduct Name : {product_name} | Price: {price} | Quantity: {quantity}")

