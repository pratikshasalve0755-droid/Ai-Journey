#Program 2: Class with Methods
print("\nProgram 2: Calculator class with methods ")

"""class Calculator:
    def put_data(self):
        self.num1 =  int(input("\nEnter first number:"))
        self.num2 = int(input("Enter second number:"))

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def display(self):
        print("---------------------------------")
        print("Addition = " , self.add())
        print("Subtraction:" , self.subtract())
        print("Multiplication: " , self.multiply())
        print("Division: ", self.divide())
        print("---------------------------------")

c1 = Calculator()
c1.put_data()
c1.display()"""

class Calculator:
    def put_data(self, num1 ,num2):
        self.num1 = num1
        self.num2 = num2


    def add(self):
        return self.num1  +  self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def display(self):
        print("---------------------------------")
        print("Addition = ", self.add())
        print("Subtraction:", self.subtract())
        print("Multiplication: ", self.multiply())
        print("Division: ", self.divide())
        print("---------------------------------")


num1 =  int(input("\nEnter first number:"))
num2 = int(input("Enter second number:"))
c1 = Calculator()
c1.put_data(num1 , num2)
c1.display()




