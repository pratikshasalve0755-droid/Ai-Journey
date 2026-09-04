# Mini-Project : Smart Contact Information Extractor

print("\nSmart Contact Information Extractor")

import re

all_emails =[]
all_phones = []

current_text = ""
cleaned_text = ""

def enter_text():
    global current_text
    text = input("\nEnter Text: ").strip()

    if text == "":
        print("Please Enter Some Text!!")
        return ""

    current_text = text
    if len(text) > 50:
        print(f"\nText Saved: {text[:50]}...")
    else:
        print(f"\nText Saved: {text}")

    return text

def extract_email(text):

    if text == "":
       print("Please Enter Some Text!!")
       return []

    emails = re.findall(r"[\w.-]+@[\w.-]+\.[\w.-]+" , text)

    all_emails.clear()
    all_emails.extend(emails)

    if emails :
        print("\nEmail Found!!")
        print("\n---- Email Addresses ----")

        for i, email in enumerate(emails, start=1):
            print(f"\n{i}. {email}")

        print("-------------------------")

    else:
        print("\nEmail Not Found!!")

    return emails

def extract_phone(text):

    if text == "":
       print("Please Enter text first!")
       return []

    phones = re.findall(r"\d{10}", text)

    all_phones.clear()
    all_phones.extend(phones)

    if phones :
        print("\nPhone No. Found!!")
        print("\n---- Phone Numbers ----")

        for i, phone in enumerate(phones, start=1):
                print(f"\n{i}. {phone}")

        print("-------------------------")

    else:
        print("\nPhone Number Not Found!!")
    return phones


def show_all_info():

    print("\n========== Extracted Information ==========")

    print("\n-- List of Emails --")

    if all_emails:
        for i, email in enumerate(all_emails, start=1):
            print(f"{i}. {email}")

    else:
        print("None")

    print("----------------------------")
    print("\n-- List of Phones --")

    if all_phones:
       for i, phone in enumerate(all_phones, start=1):
            print(f"{i}. {phone}")

    else:
        print("\nNone")

    print("\n==========================================")

def clean_text(text):

    global cleaned_text

    if not text:
        print("Please Enter Some Text First!!")
        return ""


    cleaned_text = re.sub(r"[^\w\s@#.-]" , "" , text)

    print("\n---- Clean Text ----")

    print(f"\n{cleaned_text}")

    print("\n---------------------------")
    return cleaned_text

while True:

    print("\n==== Smart Contact Information Extractor ====")
    print("\nSelect an Option:")
    print("\n1. Enter Text:")
    print("2. Extract Email Addresses")
    print("3. Extract Phone Numbers")
    print("4. Show All Extracted Information")
    print("5. Clean Text ")
    print("6. Exit")
    print("----------------------------------------------")
    try:
        option = int(input("\nChoose Your Option:"))

    except ValueError:
        print("Invalid Option!!")
        continue

    if option == 1:
        enter_text()

    elif option == 2:
         extract_email(current_text)

    elif option == 3:
        extract_phone(current_text)

    elif option == 4:
        show_all_info()

    elif option == 5:
        clean_text(current_text)

    elif option == 6:
        print("\n---- Thank you for using this program!! ----")
        break

    else:
        print("\nInvalid Option!!")


