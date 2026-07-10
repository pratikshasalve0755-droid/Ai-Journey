# Mini app : Smart Delivery Management System
print("\nMini app: Smart Delivery Management System")


class Delivery:
    def deliver_package(self):
        print("\nDelivering package!")

class BikeDelivery(Delivery):
    def deliver_package(self):
        print("--------------------------------------------")
        print("Delivering package using Bike!")

class TruckDelivery(Delivery):
    def deliver_package(self):
        print("\nDelivering package using Truck!")

class DroneDelivery(Delivery):
    def deliver_package(self):

        print("\nDelivering package using drone!")
        print("--------------------------------------------")


deliveries = [BikeDelivery() , TruckDelivery() , DroneDelivery()]

for d  in deliveries :
    d.deliver_package()


