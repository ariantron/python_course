class Rect:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def get_perimeter(self):
        return (self.height + self.width) * 2

    def get_area(self):
        return self.width * self.width


r = Rect(1, 2)
p = r.get_perimeter()
print(p)
