#Mini Project:Text Analyzer pro

print("Mini Project: Text Analyzer")

sentence = input("\nsentence: ")
sentence = sentence.lower()

vowels = "aeiouAEIOU"

total_char = 0
total_words = 0
total_vowels = 0
total_consonants = 0
most_freq_word = 0
freq = {}

for char in sentence:
   total_char += 1

for word in sentence:
    word = word.split()
    total_words =+ 1

for vowel in vowels:
    if vowel in sentence:
        total_vowels +=1

    else:
        total_consonants += 1
max_word = " "
max_count =0

for w in word:
    if w in freq :
        freq[w] += 1
    else:
        freq[w] = 1

for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        max_word = key


print("\n------Text Analysis-------")
print("Total Characters:" , total_char)
print("Total Words: " ,total_words )
print("Total Vowels :" ,total_vowels )
print("Total Consonants:" ,total_consonants )
print("Most Frequent Word:" ,max_count)








