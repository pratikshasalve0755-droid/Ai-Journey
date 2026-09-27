# Program 1: Employee Access System
print("Program 1: Employee Access System ")


from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self , name , salary):
        self.name = name
        self.__salary = salary   # private

    @abstractmethod
    def work(self):
        pass

    def get_salary(self):
        return self.__salary


class Developer(Employee):
    def work(self):
        return (f"\nDeveloper {self.name} works on writing , "
                f"debugging code and building applications. "
                f"Salary: {self.get_salary()}.")


class Designer(Employee):
    def work(self):
        return (f"Designer {self.name} Works on the UI/UX ,"
                f"graphics and layouts of application"
                f"Salary: {self.get_salary()}.")

class Manager(Employee):
    def work(self):
        return (f"Manager {self.name} handles team ,"
                f"arrange meetings , manage projects."
                f"Salary: {self.get_salary()}.")


developer = Developer("Pratiksha" , 10000)
designer = Designer("siddhi "  , 12000)
manager = Manager("shrutee" , 15000)

employee = [ developer , designer , manager ]

for emp in employee:
    print(emp.work())




