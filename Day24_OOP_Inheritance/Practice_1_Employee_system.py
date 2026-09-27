# Program 1: Employee System
print("Program 1: Employee System")

class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary


    def display_info(self):
        print(f"\nEmployee Name: {self.name}")
        print(f"Salary: {self.salary}")



class Manager(Employee):
    def __init__(self ,name , salary , bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def total_salary(self ):
       return self.salary +self.bonus

print("-----------------------------")
print("\nEmployee Details:")

Emp = Employee("Nakul", 10000)
Emp.display_info()
print("\n-----------------------------")

print("\nManager Details:")

Man  = Manager( "Pratiksha" , 10000 , 2000 )
Man.display_info()
print(f"Total Salary: {Man.total_salary()}")
print("-----------------------------")
