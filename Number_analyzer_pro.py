#MinProject: Number Analyzer Pro

numbers = []
total = 0
even_count = 0
odd_count = 0
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

    total += num
    if i == 0:
        highest = num
        lowest = num
    else:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Calculate average after loop
average = total / len(numbers)

print("\n--- Number Analyzer Pro Result ---")
print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Even Count:", even_count)
print("Odd Count:", odd_count)