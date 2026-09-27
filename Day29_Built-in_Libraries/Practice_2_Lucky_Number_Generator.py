# Program 2: Lucky Number Generator
print("\nWelcome to the Lucky Number Generator")

import random

print("\nGenerate 5 random number between 1 and 100")
for i in range(5):
    print(f"Lucky Number {i+1}:  {random.randint(1,100)}")