class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def get_perimeter(self):
        return (self.height + self.width) * 2

    def get_area(self):
        return self.width * self.width


r = Rectangle(1, 2)

r_perimeter = r.get_perimeter()
r_area = r.get_area()

print('Perimeter: ' + str(r_perimeter) + "\nArea: " + str(r_area))
