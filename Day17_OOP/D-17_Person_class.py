#Program 3: class with constructor
print("\nProgram 3: person_class with constructor")


class Person:
    def __init__(self,name ,age ,gender, city):
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city

    def display(self):
        print("----------------------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"City: { self.city}")
        print("----------------------")


p1 = Person("Kim Namjoon " , 31 , "Male" , "Seoul")
p1.display()

p2 = Person("Kim Seokjin" ,32  , "Male" , "Seoul")
p2.display()

p3 = Person("Min Yoongi",34,"Male" , "Seoul")
p3.display()

p4 = Person("Jung hasoek", 34,"Male" , "Seoul")
p4.display()

p5 = Person("Kim Taehyung", 30,"Male" , "Seoul")
p5.display()

p5 = Person("Park Jimin", 30,"Male" , "Seoul")
p5.display()

p5 = Person("Jeon Jungkook", 30,"Male" , "Seoul")
p5.display()

