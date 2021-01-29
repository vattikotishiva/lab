class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"hi this is {self.name}.I am {self.age} years old.")
    def make_sound(self):
        print("meow")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"hi this is {self.name}.I am {self.age} years old.")

    def make_sound(self):
        print("woof")

cat1 = Cat("cuty",2.5)
dog1 = Dog("bunny" ,3.5)

for animal in (cat1,dog1):
    animal.info()
    animal.make_sound()