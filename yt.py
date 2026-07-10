"""students = []                                         # initialize the list
n = int(input("\nEnter no of  students:"))

for _ in range(n):
    name = input("Enter name:")
    age = int(input("Enter age:"))
    marks = int(input("Enter marks:"))
    print("----------------------")
    student = {'name': name,'age': age , 'marks': marks}
    students.append(student)

    for student in students:

        print(f"student = Name: {student['name']} | Age: {student['age']} | Marks:{student['marks']}")"""
from dataclasses import asdict

"""import csv

search_category = input("Enter the category to search:- ")
total = 0

with open("expenses.csv", "r") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        if row[1].lower() == search_category.lower():
            amount = float(row[2])
            total += amount

print("Total spending for", search_category, "is:", total)"""

"""def add_member():

    name = input("Enter Name:-").lower()
    if name.strip() == "":
        print("Name cannot be empty!")
        return

    try:
        age = int(input("Enter Age:-"))
    except ValueError:
        print("Invalid Age!")
        return
    memberships = ["Basic" , "Premium" , "VIP"]

    membership = input("Enter type of Membership:-").lower()
    if memberships in membership:
        print(f"{name} choosen {memberships} membership ")
    if membership.strip() == "":
        print("Membership type cannot be empty!")
        return


    file_exists = os.path.isfile("members.csv")

    with open("members.csv" , "a" , newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([ "Name" , "Age" , "Membership"])
        writer.writerow([ name , age ,  membership ])

    print("Members file added succesfully!")

name = "aaa"
age =22
membership = "Basic"

add_member()"""

"""#program Merge  sort list

list_1 = [1,2,3]
list_2 = [1, 3,4]

merged_list = []
i = 0
j = 0

while i <len(list_1) and j < len(list_2):
    if list_1[i] < list_2[j]:
        merged_list.append(list_1[i])
        i += 1

    else:
        merged_list.append(list_2[j])
        j += 1


merged_list += list_1[i:]
merged_list +=  list_2[j:]

print("Merged list: " , merged_list)"""


"""class ListNode(object):
   def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        i = ListNode(0)
        j = i
        while list1 and list2:
              if list1.val < list2.val:
                 j.next = list1
                 list1 = list1.next
              else:
                 j.next = list2
                 list2 = list2.next

        j = j.next

        if list1:
            j.next = list1

        else:
            j.next = list2

        return i.next

#array ,linked list ,  stack queue ."""


# Mini app : Secure Wallet System
print("Mini app : Secure Wallet System ")

class Wallet:
    def __init__(self ,name , balance):
        self.name = name
        if balance >= 0:
            self.__balance = balance
        else:
            self.__balance = 0
            print("Balance can't be negative!")

    def add_money(self , amount):
        if amount > 0:
            self.__balance += amount
            print(f"Money added! New Balance: {self.__balance}")
        else:
            print("Amount must be greater than 0!")

    def spend_money(self , amount):
        if amount <= 0 :
            print("Amount should be positive!")

        elif amount > self.__balance:
            print("Insufficient Balance")

        else:
            self.__balance -= amount
            print(f"Spent successfully! Remaining Balance: {self.__balance}")

    def check_balance(self):
        return self.__balance


if __name__ == "__main__":

    name = input("\nEnter Name: ").strip()
    balance = float(input("Enter initial Balance: "))
    person = Wallet(name , balance)

    while True:
        print("\n----- Welcome To Wallet System -----")
        print("Select option")
        print("1. Add Money")
        print("2. Spend Money")
        print("3. Check Balance")
        print("4. Exit")
        print("--------------------------------------")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice!")
            continue

        if choice == 1:
            try:
                amount = float(input("Enter Amount: "))
                person.add_money(amount)
            except ValueError:
                print("Amount should be numeric!")

        elif choice == 2:
            try:
                amount = float(input("Enter Amount: "))
                person.spend_money(amount)
            except ValueError:
                print("Amount should be numeric!")

        elif choice == 3:
            print(f"Balance: {person.check_balance()}")

        elif choice == 4:
            print("Thank you for Visiting!")
            break

        else:
            print("Invalid Choice!")



