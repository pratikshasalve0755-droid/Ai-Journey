# Program 1: Animal_sounds Using Polymorphism
print("\nProgram 1: Animal Sound")

class Animal:
    def sound(self):
        print("\n")
        print("Every Animal makes different sounds!")

class Dog(Animal):
    def sound(self):

        print("The Dog Barks")

class Cat(Animal):
    def sound(self):
        print("The Cat Meows")


animal = Animal()
animal.sound()

print("------------------")

dog = Dog()
dog.sound()

print("------------------")
cat =Cat()
cat.sound()










