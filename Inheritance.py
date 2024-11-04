#parent class
class Animal:
    #give behaviour
    def move(self):
        print("Animal is walking")

#child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
    #giving an object to class
a = Animal()



d = Dog()
d.move()
d.bark()
