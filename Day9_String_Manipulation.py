#Program 1: Reverse string (without .split())
print("Program 1: Reverse string (without .split())")

text = "pratiksha"
i = len(text)-1
reversed_text = ""

while i >= 0:
    reversed_text += text[i]
    i -= 1
print("The Reversed text:" ,reversed_text)

print("-----------------------------------------------------")

#Program 2: Count (vowels ,consonants and space)
print("Program 2: Count (vowels ,consonants and spaces)")

text = input("enter the text :")
vowels = "aeiouAEIOU"
vowels_count = 0
consonants_count = 0
spaces = 0

for char in text:
    if char in vowels:
        vowels_count += 1

    elif char == ' ':
        spaces += 1
    elif char.isalpha():
        consonants_count += 1

print("Vowels_count:", vowels_count)
print("Consonants_count:" ,consonants_count)
print("Spaces_count:",spaces)

print("-----------------------------------------------------")
#Program 3:Check whether the string is Pallindrome
print("Program 3: Check whether the string is Pallindrome")

string = input("Enter :")
i = 0
j = len(string)-1
is_palindrome =True

while i < j:
    if string[i] != string[j]:
        is_palindrome = False
        break

    i +=1
    j-=1
if is_palindrome:
    print("Palindrome")

else:
    print("Not Palindrome")
print("-----------------------------------------------------")
#Program 4:Count how many time each word appear  in the sentence
print("Program 4: Count how many time each  word appears")

text =("python is good python is powerful python is easy "
           "python is interpreter language")

text = text.lower()
text = text.split()
freq = {}

for word in text :
    if word  in freq:
        freq[word] += 1
    else:
        freq[word] =1
print("\n",freq)