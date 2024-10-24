class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return Circle.pi * self._radius ** 2

circle = Circle(5)
print(circle.area())