"""
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
--->
Overload the __add__ method in one of the classes so that it's possible
to add attributes of two instances of that class using the + operator.

- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

"""


class Table:
    def __init__(self, material, size, function):
        self.material = material
        self.size = size
        self.function = function

    def __str__(self):
        return f"This it a {self.function} table made of {self.material}, size {self.size}"


class Tangerine:
    def __init__(self, fresh, taste):
        self.fresh = fresh
        self.taste = taste

    def __str__(self):
        return f"This is a  {self.fresh}, {self.taste} tangerine."


class Door:
    def __init__(self, status='open', height=2.1):
        self.status = status
        self.height = height

    def __str__(self):
        return f"This is a {self.status} door of {self.height} m height."

    def __add__(self, other):
        things = self.height + other.size
        return things

