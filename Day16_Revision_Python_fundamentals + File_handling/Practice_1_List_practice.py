#Pragram 1: Practice-List logic
print("Program 1: Practice-List logic")


numbers = []

for i in range(5):
    number = int(input("Enter number:-"))
    numbers.append(number)
print("\nNumbers=",numbers)

highest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > highest:
        highest = num

    elif num < smallest:
        smallest = num
print("\nHighest= ", highest)
print("Smallest= " , smallest)

even_count = 0
odd_count = 0
for i in numbers:
    if i % 2 == 0:
        even_count +=1
    else :
        odd_count += 1

print("\nEven_count= ", even_count)
print("Odd_count= " , odd_count)

