class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def get_perimeter(self):
        return (self.height + self.width) * 2

    def get_area(self):
        return self.width * self.width


class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)


s = Square(5)
print(s.get_perimeter())
