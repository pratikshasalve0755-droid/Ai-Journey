# Program 3: Execution Time Decorator

print("\nProgram 3: Execution Time Decorator")


import time

def decorator(func):
    def wrapper():

        start_time = time.time()
        func()
        print(f"\n   Start Time      : {start_time}")

        end_time = time.time()
        print(f"\n   End Time        : {end_time}")
        execution_time = end_time - start_time
        print(f"\n   Execution Time  : {execution_time:.6f} sec")


        print("==========================================")
    return wrapper

@decorator
def calculate_sum():
    total = 0
    for i in range(1 , 101):
        total += i
    print(f"\n   Sum is          : {total}")

calculate_sum()

