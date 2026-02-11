#Program 1: Using  Indexing print  first and last element and also length of the  list
print("Program 1: Using  Indexing print  first and last element and also length of the  list")
print("\n")
numbers = [10 ,20, 30, 40, 50]

print("list:",numbers)               # prints whole list
print("The first element is:",numbers[0])           # print  the number at 0 index
print("The last element is :", numbers[4])           # print the nuber at index 4
print("The length of the List: ", len(numbers))      # print the length of the list

print("---------------------------------------------------------------------------------------------------------")

#Program 2: Add ,Remove ,Sort and find the highest and lowest marks of the student

marks = [78, 65, 89, 90]

marks.append(54)                       #add the marks at end of the list
print("The added marks:" ,marks)

marks.remove(65)                       #removes the specified element
print("The marks removed:", marks)

marks.pop(1)                          #removes the element of specified index
print("The marks removed:" ,marks)

marks.sort()                          #sorts the list in ascending order
print("The sorted list:",marks)

marks.sort(reverse=True)              #sorts the list in descending order
print("The sorted list:",marks)


print("The highest marks:", max(marks))    #print highest value from list

print("The lowest marks:", min(marks))    #print lowest value from list

print("---------------------------------------------------------------------------------------------------------")

#Program 3: Print students name from the list using loop  and with index number as well
print("Program 3: Print students name from the list using loop  and with index number as well")

students = ["Amit", "Bhavana", "Chetan" ,"Diya" , "Sonal"]

print("\n"
      "Display of names by For loop\n ")
for i in students:
    print("The list contains:",i)             #prints each student name using loop

print("---------------------------")
print("\n"
      "Display of names by Index\n ")
print("The name at [0] index: ",students[0])
print("The name at [1] index: ",students[1])
print("The name at [2] index: ",students[2])
print("The name at [3] index: ",students[3])
print("The name at [4] index: ",students[4])





