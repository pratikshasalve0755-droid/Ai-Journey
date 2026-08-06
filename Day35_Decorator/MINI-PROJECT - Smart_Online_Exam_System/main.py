# Mini-Project: Online Exam System
print("\nMini-Project : Smart Online Exam System")

username = "admin"
password = "python123"
marks = 0
result = ""
login_status = False
exam_completed = False
student_name = ""

def login_required(func):
    def wrapper(*args , **kwargs):
        global login_status

        if not login_status:
            print("\nPlease Login First!")
            return

        print("\nVerification Successful!")
        return func(*args , **kwargs)

    return wrapper

def login():
    global login_status , student_name

    if login_status:
        print("Already Logged In!")
        return

    user_name = input("Username:").strip()

    if not user_name:
        print("Please enter username first!")
        print("Username Required!")
        return

    pass_word = input("Password: ")

    if not pass_word:
        print("Password Required!")
        return

    if username == user_name and password == pass_word:
           print("Login Successful!")
           login_status = True
           student_name = user_name

    else:
        print("Invalid Username or Password!")


@login_required
def start_exam():

    global marks ,result ,exam_completed

    if exam_completed:
        print("Exam already completed!")
        return

    marks = 0

    print("\n* Python MCQ *")
    print("\nChoose the  Correct Option: ")
    print("Q1: Which keyword creates a function?"
          "\n1. class"
          "\n2. def"
          "\n3. return"
          "\n4. while")
    ans1 = input("Enter your choice: ").strip().lower()
    if ans1  == "def" or  ans1 == "2" :
        print("Correct ✅")
        marks +=1
    else:
        print("Incorrect ❌")

    print("\nQ2: What is type of the result of the division expression 5/2"
          "in python?"
          "\n1. int"
          "\n2. float"
          "\n3. str"
          "\n4. list ")
    ans2 = input("Enter your choice: ").strip().lower()
    if ans2  == "float"  or  ans2 == "2":
        print("Correct ✅")
        marks +=1
    else:
        print("Incorrect ❌")

    print("\nQ3: Which of the following is a valid variable name in python?"
          "\n1. 1st_variable"
          "\n2. my-variable"
          "\n3. my_variable"
          "\n4. 2variable ")
    ans3 = input("Enter your choice: ").strip().lower()
    if ans3  == "my_variable" or ans3 == "3" :
        print("Correct ✅")
        marks +=1
    else:
        print("Incorrect ❌")

    print("\nQ4:which of the following is a correct way to create  a list in Python ?"
          "\n1. my_list = {1,2,3,4}"
          "\n2. my_list = (1,2,3,4)"
          "\n3. my_list = <1,2,3,4> "
          "\n4. my_list = [1,2,3,4]")
    ans4 = input("Enter your choice: ").strip().lower()
    if ans4  == "my_list = [1,2,3,4]" or ans4 == "4" :
        print("Correct ✅")
        marks +=1
    else:
        print("Incorrect ❌")

    print("""Q5:
    for i in range(2):
        print(i)

    1. 0,1
    2. 1,2
    3. 0,1,2
    4. 1,2,3
    """)
    ans5 = input("Enter your choice: ").strip().lower()
    if ans5 in ["1", "0,1"]  :
        print("Correct ✅")
        marks +=1
    else:
        print("Incorrect ❌")

    if marks >= 3:
        result = "Passed"
        print(f"Result : {result}!")

    else:
        result = "Failed"
        print(f"Result : {result}!")
    exam_completed = True

def view_result():
    global exam_completed
    if not exam_completed:
        print("Please complete the exam first to view your result.!")
        return

    if not login_status:
        print("Please login first to view your result.!")
        return

    else:
        print("\n========= RESULT =========")
        print(f"Student Name : {student_name}")
        print(f"Marks        : {marks}")
        print(f"Result       : {result} ")
        print("=========================")


while True:
    print("\n=================================")
    print("Welcome to Smart Online Exam System")
    print("===================================")
    print("\n1. Login")
    print("2. Start Exam")
    print("3. View Result")
    print("4. Exit")

    try:
      option = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid Option!")
        continue

    if option == 4:
        print("Thanks for Visiting!")
        break

    if option == 1:
        login()

    elif option == 2:
       start_exam()

    elif option == 3:
        view_result()

    else:
        print("Invalid Option!")