# Program 1: Check weather the number is Even or Odd

num = int (input ("Enter  a  number:"))              #input from the user
if num % 2 == 0:
    print ("Number is Even")
else:
    print("Number is Odd")

----------------------------------------------------------------------------------------------------------

#Program 2: Check weather the persons age is eligible to vote or not

Age = int(input("Enter your Age:"))
if Age >= 18:
    print("You're Eligible to Vote!")
else:
    print("You're Not Eligible to Vote!")

----------------------------------------------------------------------------------------------------------

#Program 3:  Print numbers  from 1 to 50

for i in range(1, 51):
    print(i)

----------------------------------------------------------------------------------------------------------

#Program 4: Sum of first N numbers

num = int(input(" Enter a Number:"))

total = 0
i = 1
while i <= num:
        total += i
        i += 1
print(" The sum of N numbers is:",total)

-----------------------------------------------------------------------------------------------------------

#Program 5: Login check of Users (Username , Passward)

users = {"Rutu" : "rut_5" , "savi" : "s@vi88"}
attempts = 3

while attempts > 0:
    username = input(" Enter Username:")
    passward = input(" Enter passward:")
    if username in users and users[username] == passward:
        print (" Login Successfully!")
    else:
        attempts-= 1
        print("Invalid Credensials")
else:
    print(" Login Failed!")


-----------------------------------------------------------------------------------------------------------


