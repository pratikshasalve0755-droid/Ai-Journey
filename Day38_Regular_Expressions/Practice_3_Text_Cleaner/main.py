#Program 3: Text Cleaner
print("\nProgram 3: Text Cleaner")


import re

text = input("\nEnter Text:")
print()
print(re.sub(r"\W+", " " , text))
