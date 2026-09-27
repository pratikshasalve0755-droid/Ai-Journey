# Program 2: Employee_class with class variable
print("Program 2: Employee class with class variable")


class Employee:
    company = "ABC Pvt.Ltd"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amoount

    def display(self):

        print("-----------------------------------------------")
        print(self.name,"  |", self.salary ,"  |",  Employee.company)

print("\nName", "       |", "Salary", "  |" , "Company")
e1 = Employee("Pratiksha" , 200000)
e2 = Employee("Radhik   " , 100000)
e3 = Employee("Vikashar " , 200000)
e4 = Employee("Pruthvik ", 100000)
e1.display()
e2.display()
e3.display()
e4.display()

