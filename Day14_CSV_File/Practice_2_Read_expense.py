#Program 2:Read_expenses

import csv
with open("expenses.csv" , "r") as file:
  csv_reader = csv.reader(file)
  for row in csv_reader:
      print(row)


"""with open("expenses.csv" , "w" , newline="") as  file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['date' , 'category' ,'amount' , 'description'])"""
