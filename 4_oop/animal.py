class Animal:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender


class Bird(Animal):
    birds = ["Hawk", "Eagle", "Swan"]

    def __init__(self, name, gender):
        super().__init__(name, gender)

    def is_bird(self):
        return self.name in Bird.birds

    def fly(self):
        if self.is_bird():
            print(self.name + " has been flied!")
        else:
            print(self.name + " can't fly!")


b = Bird("Pan", "male")
b.fly()
