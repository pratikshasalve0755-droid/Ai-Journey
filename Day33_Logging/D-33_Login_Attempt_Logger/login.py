# Program 3: Login Attempt Logger
print("\nProgram 3: Login Attempt Logger ")

import logging

username = "admin"
password = "python123"
failed_attempts = 0

logging.basicConfig(
    filename = "Login.log",
    level = logging.DEBUG,
    filemode = "a",
    format = '%(asctime)s - %(levelname)s - %(message)s'
)



while True:
    user_name = input("\nEnter Username: ").strip()
    pass_word = input("Enter Password: ").strip()

    if user_name == username and pass_word == password:
       logging.info(f"User '{user_name}' logged successfully!")
       print("Login Successfully!")
       break

    else:
       failed_attempts += 1
       print("Incorrect Password!")
       logging.warning(f"Invalid login attempt for username: '{user_name}'")
       if failed_attempts >= 3:
          print("Too many failed attempts!")
          logging.critical("Three consecutive failed login attempts detected")
          break
