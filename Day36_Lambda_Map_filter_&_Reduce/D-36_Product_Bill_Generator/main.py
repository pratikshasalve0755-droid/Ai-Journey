#Program 3: Product Bill Generator
print("\nProgram 3: Product Bill Generator")


from functools import reduce

prices = [250, 450, 300, 150]

total_amount = reduce(lambda x , y : x+y ,prices )
print(f"\nprices: {prices}")
print("Total Bill Amount:" , total_amount)