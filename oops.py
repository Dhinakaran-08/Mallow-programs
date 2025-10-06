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
obj = Parent()
obj.age()
obj.hair()
obj.eye()