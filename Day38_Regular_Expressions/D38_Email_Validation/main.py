#program 2: Email Validation
print("\nProgram 2: Email Validation")

import re


email = input("\nEnter email:")
print()

if re.match(r"^[\w.-]+@[\w.-]+\.[\w.-]+$", email):
    print("Valid Email!!")
else:
    print("Invalid Email")