# Mini-Project : Smart Multi-Task Data Processor
print("\nMini-Project : Smart Multi-Task Data Processor")


from threading import Thread
import time


def task_one():
    print("\nCollecting Data...")
    for i in range(1,6):
        print(f"NUMBER:- {i}")
        time.sleep(0.5)

    print("------------------------------")

def task_two():
    print("\nProcessing Data...")
    alpha = "aeiou"
    for char in alpha:
        print(f"VOWEL:- {char}")
        time.sleep(0.5)

    print("-----------------------------")

def task_three():
    print("\nGenerating Data...")
    print("\n--- BTS Members ---")
    time.sleep(0.5)
    print("\n---- HYUNG LINE ----\n1. KIM SEOK JIN 🐷\n2. MIN YOONGI 😺\n3. JUNG HOSOEK 🐿️\n4. KIM NAMJOON 🐨")
    time.sleep(0.5)
    print("\n---- MAKNAE LINE ----\n1. PARK JIMIN 🐣\n2. KIM TAEHYUNG 🐻\n3. JEON JUNGKOOK 🐰")
    time.sleep(0.5)
    print("\n--------------------------------")

def run_sequential():
    task_one()
    task_two()
    task_three()


def run_multithreading():
    t1 = Thread(target = task_one)
    t2 = Thread(target = task_two)
    t3 = Thread(target = task_three)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

sequential_time = None
multithreading_time = None


while True:
    print("\n=========================================")
    print("   Smart Multi-Task Data Processor   ")
    print("=========================================")

    print("\nSelect Option")
    print("1. Run Task Sequentially")
    print("2. Run Task Using Threads")
    print("3. Measure Execution Time")
    print("4. Exit")
    print("\n----------------------------------------")

    try:
        option = int(input("\nEnter Option:"))

    except ValueError:
        print("Invalid Option")
        continue

    if option == 1:
        start_time = time.perf_counter()

        run_sequential()

        end_time = time.perf_counter()

        sequential_time = end_time - start_time

        print(f"\nSequential Time : {sequential_time:.2f}")

    elif option == 2:
        start_time = time.perf_counter()

        run_multithreading()

        end_time = time.perf_counter()

        multithreading_time = end_time - start_time

        print(f"Multi-threading Time :  {multithreading_time:.2f}")

    elif option == 3:
        if sequential_time is  None and multithreading_time is None:
            print("\nFirst run Option 1 or Option 2.")

        else:

            print("\n========== Execution Time ==========")

            if sequential_time is not None:
                print(
                    f"Sequential Time     : "
                    f"{sequential_time:.2f} seconds"
                )
            else:
                print("Sequential Time     : Not measured")

            if multithreading_time is not None:
                print(
                    f"Multithreading Time : "
                    f"{multithreading_time:.2f} seconds"
                )
            else:
                print("Multithreading Time : Not measured")

            print("====================================")

    elif option == 4:
        print("\nExiting... ")
        break

    else:
        print("Invalid Option")