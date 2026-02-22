#Program 1: Print sum ,average ,largest and smallest from the list
print("Program 1: Print sum, average, largest and smallest numbers from list")

numbers = []
for i in range (5):
    num = int(input("Enter number:"))
    numbers.append(num)
print("\nNumbers = " ,numbers)

total = 0
highest =numbers[0]
smallest =numbers[0]

for num in numbers:
        total += num
        if num > highest:
            highest = num

        if num < smallest:
            smallest = num

average = total/len(numbers)
print("Average =" ,average)
print("Total = ", total)
print("Smallest =",smallest)
print("Highest =", highest)

print("------------------------------")

#Program 2: Remove Duplicates from the list
print("Program 2: Remove Duplicate from the list")

numbers = [11,56,78,45,99,67,56,97,88,56,43,22,99]
unique = []
print("Numbers = " ,numbers)

for num in numbers:
    if num  not in  unique:
        unique.append(num)

print("Unique =" , unique)

print("------------------------------")

#Program 3: Merge two lists into one
print("Program 3: Merge two lists")

list_1 = []
list_2 =[]

for i in range(3):
    n = input("Enter names:")
    list_1.append(n)
print("\nList_1 = " , list_1)

for j in range(4):
    m = input("Enter names:")
    list_2.append(m)
print("\nList_2 =" ,list_2)

list_3 = list_1 + list_2
print("\nList =" ,list_3)

print("------------------------------")
#Program 4:Sort thr list manually(without sort())
#using Bubble sort logic
print("Program 4: Sort the list")

num = [5 ,1 ,2, 4 ,8]

n = len(num)
print("Length of list:" ,n)

for  i in range(n-1):
    for j in range(n-1-i):
        if num[j] > num[j+1]:
           num[j] , num[j+1]  = num[j +1] , num[j]
print("Sorted List: " , num)

print("------------------------------")

#Using Selection sort logic

num = [5 ,1 ,2, 4 ,8]
n= len(num)

print("Length of list:",n)

for i in range(n-1):
    min_index = i
    for j in range(i+1 ,n):
        if num[j] < num[min_index]:
            min_index = j
    if min_index != i:
            num[i] ,num[min_index] = num[min_index] ,num[i]

print ("Sorted List",num)






