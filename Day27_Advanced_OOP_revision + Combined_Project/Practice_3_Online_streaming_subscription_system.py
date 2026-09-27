# Program 3: Online Streaming Subscription System
print("\nProgram 3: Online Streaming Subscription System ")


from abc import ABC , abstractmethod
class Subscription(ABC):
    def __init__(self , subscription_id):
        self.__subscription_id = subscription_id

    def show_subscription(self):
        return f"Subscription ID : {self.__subscription_id}"

    @abstractmethod
    def watch_content(self):
        pass

class BasicPlan(Subscription):
    def __init__(self, subscription_id):
        super().__init__(subscription_id)
    def watch_content(self):
        return "Watching The content with Basic plan!"


class PremiumPlan(Subscription):
    def __init__(self, subscription_id):
        super().__init__(subscription_id)

    def watch_content(self):
        return "Watching The content with Premium plan with HD Quality!"

class FamilyPlan(Subscription):
    def __init__(self, subscription_id):
        super().__init__(subscription_id)

    def watch_content(self):
        return "Watching the content with family member simultaneously!"

basic = BasicPlan("SUB101")
premium = PremiumPlan("SUB201")
family = FamilyPlan("SUB301")

plan = [basic , premium , family]

for p in plan:
    print("-----------------------------")
    print(p.show_subscription())
    print(p.watch_content())





