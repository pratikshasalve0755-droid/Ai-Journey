# Mini Project: Smart Vehicle Control System
print("Mini Project: Smart Vehicle Control System")


from abc import ABC , abstractmethod
class Vehicle(ABC):
    def __init__(self , brand):
        self.brand = brand

    def get_brand(self):
        return f"The Vehicle is of {self.brand} Company."

    @abstractmethod
    def start_engine(self):
        pass

    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self , brand ,works_on):
        super().__init__( brand)
        self.works_on = works_on

    def start_engine(self):
        return f"The {self.brand} Car works on {self.works_on} and it is started."

    def stop_engine(self):
        return f"The {self.brand} car gets stop."

class Bike(Vehicle):
    def __init__(self,brand , works_on):
        super().__init__(brand)
        self.works_on = works_on

    def start_engine(self):
        return f"The {self.brand} Bike works on {self.works_on} and it started."

    def stop_engine(self):
        return f"The {self.brand} bike gets stop."

class Truck(Vehicle):
    def __init__(self,brand, works_on , load_capacity):
        super().__init__(brand)
        self.works_on = works_on
        self.load_capacity = load_capacity

    def start_engine(self):
        return f"The {self.brand} Truck works on {self.works_on} and it started."

    def stop_engine(self):
        return f"The {self.brand} truck gets stop."

print("\n----- Car Details ------")
car = Car("Tesla" , "Electric")
print(car.get_brand())
print(car.start_engine())
print(car.stop_engine())
print("\n------- Bike Details ------")
bike = Bike("Honda" , "Petrol")
print(bike.get_brand())
print(bike.start_engine())
print(bike.stop_engine())
print("\n------- Truck  Details ------")
truck = Truck("Tata" , "Diesel" , 15)
print(truck.get_brand())
print(truck.start_engine())
print(truck.stop_engine())



