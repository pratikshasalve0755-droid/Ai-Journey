
word = 'python is fun ,python is easy , python is fun'
word = word.strip().lower()
count = 0

target = input("enter a word:")

for char in word:
    if char.isalpha() == target:
        count += 1

print(count)
