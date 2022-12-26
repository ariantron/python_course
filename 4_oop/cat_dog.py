class Animal:
    def __init__(self, name):
        self.name = name

    def to_string(self):
        return self.name


class Mammal(Animal):

    def __init__(self, name):
        super().__init__(name)

    def greets(self):
        return self.name + " greets!"


class Cat(Mammal):

    def __init__(self):
        super().__init__("Cat")

    def greets(self):
        return "MEW MEW"


class Dog(Mammal):

    def __init__(self):
        super().__init__("Dog")


dog = Dog()
print(dog.greets())
