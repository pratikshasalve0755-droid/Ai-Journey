#Program 1: Take a list Return:Total,Average,Largest and Smallest
print("Program 1: Take a list Return: Total , Average,largest and smallest")

def analyze_marks(marks_list):
  total = 0
  largest =marks_list[0]
  smallest =marks_list[0]

  for marks in marks_list:
       total += marks

       if marks > largest:
            largest = marks

       if marks < smallest:
            smallest = marks

  average = total/len(marks_list)
  return total, largest,smallest ,average

marks_list= [67, 23, 45, 34, 56]
total, largest,smallest ,average = analyze_marks(marks_list)

print("marks_list:",marks_list)
print(f"Total marks: {total}")
print(f"Largest: {largest}")
print(f"smallest:{smallest}")
print(f"Average:{average}")

print("---------------------------------------------------------------")

#Program 2: create a function take a number returns whether its Prime number or not
print("Program 2: Create a function take a number and return whether its Prime or not")

def check_prime(number):
    if  number <= 1:
         return "Not Prime"

    for i in range(2,(number //2)+1):
        if number % i == 0:
             return "Not Prime"

    return "Prime"

num = int(input("Enter number:"))
result = check_prime(num)
print(f"The number {num} is :" ,result )

print("---------------------------------------------------------------")

#Program 3:Create a function  take a string and return no. of vowels and consonants
print("Program 3:Return no. of vowels and consonants from the string")

def check_vowels(string):
    vowels =[ "a","e","i","o","u"]
    vowel_count = 0
    consonant_count = 0
    for char in string.lower():
        if char in vowels:
            vowel_count +=1

        else:
            consonant_count +=1
    return vowel_count ,  consonant_count

string =input("Enter name: ")
vowel_count , consonant_count =check_vowels(string)
print(f"The {string} contains \n {vowel_count} vowels and \n {consonant_count} consonants ")








