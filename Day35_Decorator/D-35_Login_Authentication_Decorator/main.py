# Program 2: Login  Authentication Decorator
print("\nProgram 2: Login Authentication Decorator!")

is_logged_in = False

def decorator(func):
    def wrapper():
        if is_logged_in:
            print("\nAccess Granted!")
            func()

        else:
            print("\nAccess Denied!")

    return wrapper
@decorator
def show_dashboard():
    print("Welcome to the Dashboard !")

print("\nLogin Status: " , is_logged_in)
show_dashboard()


# Program 2: Login Authentication Decorator
print("\nProgram 2: Login Authentication Decorator!")

is_logged_in = False


def decorator(func):
    def wrapper():
        if is_logged_in:
            print("\nAccess Granted!")
            func()
        else:
            print("\nAccess Denied!")
    return wrapper


def show_dashboard():
    print("Welcome to the Dashboard!")


# Python internally does this
show_dashboard = decorator(show_dashboard)

print("Login Status:", is_logged_in)

show_dashboard()