# Program 3:Appliance System
print("Program 3: Appliance system ")

from abc import ABC , abstractmethod
class Appliance(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):
    def __init(self):
        super().__init__()
        return

    def turn_on(self):
        return "\nPlease Turn On the Fan"

class AC(Appliance):
    def __init__(self):
        super().__init__()
        return

    def turn_on(self):
        return "Please Turn On the AC"


class WashingMachine(Appliance):
    def __init__(self):
        super().__init__()
        return

    def turn_on(self):
        return "Please Turn On the Washing Machine"


fan =Fan()
print(fan.turn_on())

ac = AC()
print(ac.turn_on())

wm = WashingMachine()
print(wm.turn_on())