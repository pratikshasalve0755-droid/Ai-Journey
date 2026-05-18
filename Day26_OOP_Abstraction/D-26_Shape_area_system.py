# Program 1: Shape Area System
print("Program 1: Shape Area System")

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self , shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self , length , breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(Shape):
    def __init__(self , radius):
        super().__init__("Circle")
        self.radius = radius


    def area(self):
        return  math.pi * self.radius


class Triangle(Shape):
    def __init__(self , base , height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return  0.5 * self.base * self.height



R = Rectangle( 3 , 5 )
print( f"\nThe Area of Rectangle = {R.area()}")

C =Circle( 5)
print(f"The Area of Circle = {C.area():.2f}")

T = Triangle( 5 , 10)
print(f"The Area of Triangle = {T.area()}")




