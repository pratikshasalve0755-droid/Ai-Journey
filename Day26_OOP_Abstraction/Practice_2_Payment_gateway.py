# Program 2: Payment Gateway
print("Program 2: Payment Gateway")

from abc import ABC , abstractmethod
class Payment(ABC):
    def __init__(self , amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def __init(self , amount):
        super().__init__(amount)

    def pay(self):
        return f"\n{self.amount} rupees paid using UPI"

class CreditCard(Payment):
    def __init__(self ,amount):
        super().__init__(amount)

    def pay(self):
        return f"{self.amount} rupees paid using Credit Card"

class NetBanking(Payment):
    def __init__(self, amount ):
        super().__init__(amount)

    def pay(self):
            return (f"{self.amount} rupees paid using Net Banking")

upi = UPI( 100)
print(upi.pay())

cc = CreditCard(100)
print(cc.pay())

NB = NetBanking(100)
print(NB.pay())


