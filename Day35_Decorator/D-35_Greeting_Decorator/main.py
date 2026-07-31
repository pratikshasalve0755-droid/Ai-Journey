# Program 1: Greeting Decorator
print("\nProgram 1: Greeting Decorator")


def decorator(func):
    def wrapper():
        print("\n==========================")
        print("     Program Started        ")
        print("==========================")
        func()
    return wrapper

@decorator
def greet():
    print("\nHello , Welcome!")

greet()



