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


door_1 = Door('open', 3)
door_2 = Door('shut', 1)
door_3 = Door('closed', 2.5)
door_4 = Door()

tangerine_1 = Tangerine('rotten', 'bitter')
tangerine_2 = Tangerine('fresh', 'sweet')
tangerine_3 = Tangerine('rotten', 'awful')

table_1 = Table('wood', 1.1, 'bedside')
table_2 = Table('metal', 0.9, 'dinner')
table_3 = Table('wood', 1, 'dinner')

print(door_4)
door_4.status = 'shut'
print(door_4)
print(tangerine_2)
tangerine_2.fresh, tangerine_2.taste = 'rotten', 'awful'
print(tangerine_2, 'You should have eaten faster!')
print(door_2)
door_2.height = door_2.height * 2
print(door_2)
print('If you put a door on a table, the added height will be',
      door_2.__add__(table_3))
