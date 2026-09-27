#Program 2: Product_analysis.py
print("Program 2: Product Analysis ")

import csv

try:
    with open("product_record.csv" , "r" , newline="") as file:
        reader = csv.reader(file)
        next(reader , None)

        found = False

        for row in reader:
            if len(row) < 3:
                print("Skipping invalid row:", row)
                continue

            product_name = row[0]

            try:
               product_price = float(row[1])
               product_quantity = int(row[2])

               total_value = product_price * product_quantity
               print(f"{product_name} : Rs.{total_value}")

               found = True

            except ValueError:
               print("Value should number!")

        if not found:
           print("Data not found")

except FileNotFoundError:
    print("file not found!")


"""with open("product_record.csv" , "w" , newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name" , "Price" , "Quantity"])"""