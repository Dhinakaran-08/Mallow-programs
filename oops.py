class Parent:
    def age(self):
        print("I am 65 years old")
    def hair(self):
        print("My hair colour is brown")
    def eye(self):
        print("My eye colour is blue")
class Child(Parent):
    def age(self):
        print("I am 30 years old")
obj = Child()
obj.age()
obj.hair()
obj.eye()

'''Inheritance'''

class Animal:
    def __init__(self,name,eye):
        self.name=name
        self.eye=eye
    def info(self):
        return f"{self.name} has four legs and {self.eye} coloured eyes"
class Dog(Animal):
    def __init__(self,name,eye):
        super().__init__(name,eye)
    def bark(self):
        return f"{self.info()} and also {self.name} is barking"
class Cat(Animal):
    def __init__(self,name,eye):
        super().__init__(name,eye)
    def meow(self):
        return f"{super().info()} and also {self.name} is meow"
dog = Dog("rocky","brown")
cat = Cat("poonachiii","blue")
print(dog.bark())
print(cat.meow())