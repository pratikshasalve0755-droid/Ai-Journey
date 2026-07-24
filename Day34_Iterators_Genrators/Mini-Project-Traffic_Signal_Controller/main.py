# Mini-Project: Smart Traffic Controller
print("\nMini Project: Smart Traffic Controller")


def traffic_signal():

    signals = [
               "Red",
               "Green" ,
               "Yellow"
               ]

    signal_time = {
        "Red": 30,
        "Green": 25,
        "Yellow": 5
    }

    current_cycle = 1

    while True:
        for state in signals:
            yield state , current_cycle , signal_time[state]

            if state == "Yellow":
               current_cycle += 1

gen = None
while True:
        print("\n===== Smart Traffic Signal Controller =====")
        print("\nSelect an option:")
        print("1. Start Traffic Signal")
        print("2. Show Next Signal")
        print("3. Restart Cycle")
        print("4. Exit")
        print()

        try:

           option = int(input("Choose an Option:"))

        except ValueError:
           print("Invalid Option!")
           continue

        if option == 4:
           print("Thank you for using Smart Traffic Controller!")
           break

        if option == 1:
            gen = traffic_signal()
            print("🚦Traffic Signal Started!!")

        elif option == 2:
            if gen is None:
                print("Please start the traffic signal first (Option 1)!")
                continue

            try:
                state, current_cycle ,remaining_time = next(gen)
                print("\n========== Traffic Signal ==========")
                print(f"\n🚦 Current Cycle: {current_cycle}")
                print(f"\n🚥 Current Signal : {state}")
                print(f"\n⌛ Time Remaining: {remaining_time} sec")
                print("\n====================================")


            except StopIteration:
                break

        elif option == 3:

            gen = traffic_signal()
            print("Traffic Signal Restarted Successfully!")

        else:
            print("Invalid Option!")