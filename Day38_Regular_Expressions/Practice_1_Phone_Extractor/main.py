#Program 1:  Extract Phone Numbers
print("\nProgram 1: Extract Phone Numbers")


import re


text = """
Contact Rahul at 9876543210.
Aarti: 9123456789.
Office: 9988776655
"""

print(re.findall(r"\d{10}", text))



