# Program 2: Vehicle System
print(" Program 2: Vehicle System")

class Vehicle:
    def __init__(self, brand , speed):
        self.brand = brand
        self.speed = speed

    def show_details(self):
        print(f"Brand : {self.brand}")
        print(f"Speed : {self.speed}")


class Car(Vehicle):
    def __init__(self , brand , speed ,fuel_type):
        super().__init__( brand , speed )
        self.fuel_type = fuel_type

    def show_details(self):
        super().show_details()
        print(f"Fuel-Type : {self.fuel_type}")

class Bike(Vehicle):
    def __init__(self , brand , speed ,  helmet):
        super().__init__(brand , speed)
        self.helmet = helmet

    def show_details(self):
        super().show_details()
        print(f"Helmet : {self.helmet}")

print("-----------------------------")

V = Vehicle("Generic Vehicle" , 70)
C = Car("Toyoto" , 120 , "Petrol")
B = Bike("Honda" , 50 , "Required")

print("Vehicle Details :- ")
V.show_details()
print("-----------------------------")

print("Car Details :- ")
C.show_details()
print("-----------------------------")

print("Bike Details :- ")
B.show_details()
print("-----------------------------")

