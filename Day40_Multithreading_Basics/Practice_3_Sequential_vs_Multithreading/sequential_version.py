# Program 3: Sequential Vs Multithreading
print("\nProgram 3: Sequential Version")


import time

def breakfast():
    print("\nTask 1 Started ...")
    print("\n=> Lets Eat Aloo Paratha For Breakfast😋")
    time.sleep(1)
    print("\nTask 1 Finished ...")
    print("-----------------------------------------")
def study():
    print("\nTask 2 Started ...")
    print("\n=> Today I Am Learning Multi-Threading")
    time.sleep(1)
    print("\nTask 2 Finished")
    print("---------------------------------------------")
def dinner():
    print("\nTask 3 Started ...")
    print("\n=> Lets Eat Rajma Chawal For Dinner😋")
    time.sleep(1)
    print("\nTask 3 Finished ...")

    print("------------------------------------")

breakfast()
study()
dinner()
