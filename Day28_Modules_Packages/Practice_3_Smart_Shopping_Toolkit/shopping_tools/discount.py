
def apply_discount():
    original_price = float(input("Enter price:"))
    discount_amt = float(input("Enter discount amount :"))

    return original_price , discount_amt

def final_price(original_price , discount_amt):
    return original_price - discount_amt

def display_result(original_price , discount_amt , result):
    print("\n----- BILL SUMMARY -----")
    print(f"Original Price : {original_price}")
    print(f"Discount : {discount_amt}")
    print(f"Final Price : {result}")



