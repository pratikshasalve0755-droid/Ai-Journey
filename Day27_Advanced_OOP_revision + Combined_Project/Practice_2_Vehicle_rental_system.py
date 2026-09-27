# Program 2: Vehicle Rental System
print(" Program 2: Vehicle Rental System")


class Vehicle:
    def __init__(self , vehicle_no ):
        self.__vehicle_no = vehicle_no

    def show_vehicle(self):
        return f"Vehicle Number : {self.__vehicle_no}"

class Car(Vehicle):
    def rent(self):
        return "Car of Rented Successfully for Family travel."


class Bike(Vehicle):
    def rent(self):
        return "Bike of Rented Successfully for quick city travel."

class Bus(Vehicle):
    def rent(self):
        return "Bus of Rented Successfully for school picnic."

car = Car("MH 12 QB 1234")
bike = Bike("MH 22 PS 4567")
vb = Bus("MH 32 kk 7896")


vehicle = [car , bike , vb]

for v in vehicle:
    print("--------------------------")
    print(v.show_vehicle())
    print(v.rent())




