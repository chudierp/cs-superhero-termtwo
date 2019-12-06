class Animal:
    def __init__(self, name):
        
       self.name = name

    def eat(self):
        print(self.name, "is eating")
    
    def drink(self):
         print(self.name, "is drinking")

class Frog(Animal):
    def jump(self):
        print(self.name, "is jumping")

animal = Animal("George")
frog = Frog("Yg")
animal.eat()
animal.drink()
frog.jump()