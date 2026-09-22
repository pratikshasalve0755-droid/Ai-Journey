#Program 3: Sequential VS Multithreading
print("\nProgram 3: Multithreading Versions")

from threading  import Thread
import time


def breakfast():
    print("\nTask 1 Started ...")
    print("\n=> Lets Eat Aloo Paratha For Breakfast😋")
    time.sleep(1)
    print("\nTask 1 Finished ...")

def study():
    print("\nTask 2 Started ...")
    print("\n=> Today I Am Learning Multi-Threading")
    time.sleep(1)
    print("\nTask 2 Finished")

def dinner():
    print("\nTask 3 Started ...")
    print("\n=> Lets Eat Rajma Chawal For Dinner😋")
    time.sleep(1)
    print("\nTask 3 Finished ...")



t1 = Thread(target = breakfast)
t2 = Thread(target = study)
t3 = Thread(target = dinner)


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()