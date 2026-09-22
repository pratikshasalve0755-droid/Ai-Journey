#Program 2: Multi Threading
print("\nProgram 2: Multi Threading")


import time
from threading import Thread

def print_numbers():

    print("\n--- print_numbers Task Start ---")
    for i in range(1, 6):
        print(i)
        time.sleep(0.5)
    print("\nPrinting message Finished.........")

t1 = Thread(target = print_numbers)

def display_message():

    print("\n--- display_message Task Start ---")

    print("\nHello")
    time.sleep(0.5)
    print("Korea Is Waiting For You Babe ❤️.........")
    time.sleep(0.5)
    print("Byeeeee..........")

    print("\nDisplaying Message Finished.........")

t2 = Thread(target = display_message)


def count_numbers():
    print("\n--- count_numbers Task Start ---")
    for i in range(1, 6):

        print(f"\nCount : {i}")
        time.sleep(1)
    print("\nPrinting Numbers Finished........")

t3 = Thread(target = count_numbers)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()




