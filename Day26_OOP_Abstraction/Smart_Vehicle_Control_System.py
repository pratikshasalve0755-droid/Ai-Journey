# Mini Project: Smart Vehicle Control System
print("Mini Project: Smart Vehicle Control System")


from abc import ABC , abstractmethod

class Vehicle(ABC):
    def __init__(self , brand , works_on):
        self.brand = brand
        self.works_on = works_on

    def get_brand(self):
        return f"The Vehicle belongs to {self.brand} Company."

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):

    def start_engine(self):
        return f"The {self.brand} Car works on {self.works_on} and engine started."

    def stop_engine(self):
        return f"The {self.brand} car engine stopped."

class Bike(Vehicle):

    def start_engine(self):
        return f"The {self.brand} Bike works on {self.works_on} and it started."

    def stop_engine(self):
        return f"The {self.brand} bike engine stopped."

class Truck(Vehicle):
    def __init__(self,brand, works_on , load_capacity):
        super().__init__(brand , works_on)
        self.works_on = works_on
        self.load_capacity = load_capacity

    def start_engine(self):
        return (
            f"The {self.brand} truck works on {self.works_on} "
            f"and can carry {self.load_capacity} tons."
        )

    def stop_engine(self):
        return f"The {self.brand} truck engine stopped."


car = Car("Tesla" , "Electric")
bike = Bike("Honda" , "Petrol")
truck = Truck("Tata" , "Diesel" , 15)

Vehicles = [ car, bike ,truck ]

for  v in Vehicles:
    print("\n-------------------")
    print(v.get_brand())
    print(v.start_engine())
    print(v.stop_engine())




