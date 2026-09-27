#Program 3: Product Price Processor
print("\nProgram 3: Product Price Processor")

products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 800},
    {"name": "Keyboard", "price": 1500},
    {"name": "Monitor", "price": 12000},
    {"name": "USB Cable", "price": 400}
]


names = [ item['name'] for item in products ]
premium_products = [ i for i in products if i['price']  > 1000 ]

discounted_price = [{'name' : x['name'] , "Original Price" : x['price'] , "Discounted Price" : x['price'] * 0.90}
                    for x in products ]

print("\n==========================================")
print(f"\nName : {names}")
print("-------------------------------------")
print(f"\nPremium Products: {[p['name'] for p in premium_products ]}")
print("----------------------------------------------------------")
print(f"\nDiscounted Products:")
for d in discounted_price:
    print(f"\n{d['name']} : {d['Original Price']}" )
    print(f"{d['name']} : {d['Discounted Price']}")
    print("------------------------------------------")