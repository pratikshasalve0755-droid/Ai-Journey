#Program 1: print each number from the list and also square of each element
print("Program 1: print each number from the list and also square of each element")

num =  [2,3,4, 5]

print("\nlist=" ,list)

for x in num:
    square = x ** 2
    print (f"square of {num} is {square}")

print("------------------------------------------------------------------------------------")

#Program 2: Count number of the even and odd from the list
print("Program 2: Count number of the even and odd from the list")

numbers =[ 92, 56, 67, 33, 77, 54, 88, 79, 31, 55]
print("\nlist=" ,numbers)

even =  0
odd = 0

for x in numbers:

    if x % 2==0:
        even += 1

    else:
        odd += 1
print("The count of even numbers:" ,even)
print("The count of odd numbers:" ,odd)


print("------------------------------------------------------------------------------------")

#Program 3:Find the largest number and second largest number from the list  WITHOUT using max()
print("Program 3:Find the largest number from the list  WITHOUT using max()")

numbers =[ 12, 56, 67, 33, 98, 54, 88, 79, 31, 55]

first_largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > first_largest:
        second_largest = first_largest
        first_largest = num

    elif   num > second_largest and num != first_largest:
        second_largest =num

print("the first largest number  is:", first_largest)
print("the second largest number is :",second_largest)

print("------------------------------------------------------------------------------------")

#Program 4: Reverse a List (Without reverse())
print("Program 4: Reverse a List (Without reverse())")

num= [ 1, 2, 3, 4, 5]
start =0
end =len(num)-1
while start < end:
    num[start] ,num[end] = num[end] ,num[start]
    start +=1
    end -=1

print ("The Reverse list:",num)

print("------------------------------------------------------------------------------------")

#Program 5: Count positive,zeros and negative from the list
print("Program 5: Count positive,zeros and negative from the list")

numbers=[3, -1, 0, 5, -2, 0, 8,-4, 6, 5, 2, -9 ,0 ]

positive = 0
negative = 0
zeros = 0

for num in numbers:
    if num == 0:
        zeros += 1
    elif  num > 0:
        positive += 1
    else:
        negative += 1

print("The count of zeros :" ,zeros)
print("The count of Positive numbers:", positive)
print("The count of Negative numbers:" ,negative)

print("------------------------------------------------------------------------------------")

#Program 6: Remove the duplicates from the list  (WITHOUT set())
print("Program 6: Remove the duplicates from the list (WITHOUT set())")

numbers=[3, 1, 0, 5, 2, 6, 8,4, 6, 5, 2, 9 ,0 ]

result =[]
for num in numbers:
    if num not in result:
        result.append(num)
print("list without duplicate elements:", result)

print("------------------------------------------------------------------------------------")

#Program 7: Pattern Printing using Nested loops
print("Program 7: Pattern Printing using Nested loop")

for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
print("------------------------------------------------------------------------------------")

for i in range (1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

print("------------------------------------------------------------------------------------")

for i in range(6,0,-1):
    for j in range(i-1):
        print("*", end=" ")
    print()

print("------------------------------------------------------------------------------------")

rows=6
for i in range (1,rows+1):
        print(" "*(rows-i)*2, end="  ")
        for j in range(i):
            print("*", end="    ")
        print()

print("------------------------------------------------------------------------------------")

"""rows=6
for i in range (5,rows-1):
        print(" "*(rows-i)*2, end="  ")
        for j in range(i):
            print("*", end="    ")
        print()"""
print("------------------------------------------------------------------------------------")

for i in range(1,6):
    for j in range(1,i+1):
        print( j , end =" ")
    print()

print("------------------------------------------------------------------------------------")

#Program 8:Frequency Counter
print("Program 8: Frequency Counter")

numbers =[3, 1,1,2, 2,3]

visited = []
for num in numbers:
    if num not in visited:
        count =0
        for n in numbers:
            if num == n:
               count+=1

        print(num ,"--", count , "times"  )
        visited.append(num)


