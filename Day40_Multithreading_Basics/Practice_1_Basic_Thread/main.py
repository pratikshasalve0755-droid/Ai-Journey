# Program 1: Basic Thread
print("\nProgram 1: Basic Thread")


from threading import Thread


def display():

    for i in range(1):
        print("\nHELLO!!")

t1=Thread(target = display)
print("\nTASK STARTED!")
t1.start()
t1.join()
print("\nTASK FINISHED!")

