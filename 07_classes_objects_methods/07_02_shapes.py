'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'The circle with a radius of {self.radius}'

    def area(self):
        area = self.radius**2 * 3.14
        return area

    def circumference(self):
        circum = 2 * 3.14 * self.radius
        return circum


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f'The rectangle with width {self.width} and length {self.length}'

    def area(self):
        area = self.width * self.length
        return area

    def perimeter(self):
        perimeter = 2 * (self.width + self.length)
        return perimeter


c_a = Circle(3)
r_a = Rectangle(3, 4)
print(f'{c_a}, area {c_a.area()}, circumference {c_a.circumference()}')
print(f'{r_a}, area {r_a.area()}, perimeter {r_a.perimeter()}')

