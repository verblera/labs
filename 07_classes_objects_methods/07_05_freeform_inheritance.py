"""
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

"""


from freeform import Table, Door


class TableToSell(Table):

    def __init__(self, material, size, function, price, state='as new'):
        super().__init__(material, size, function)
        self.price = price
        self.state = state

    def sell(self):
        self.state = 'sold'

    def __str__(self):
        return f'This table is for sale. Price {self.price:.2f}, {self.state}'


class TableSale(TableToSell):

    def sale(self):
        self.price = 0.95 * self.price


class EntranceDoor(Door):
    def rob(self):
        self.status = 'open'
        print(f"Alert! Alert! This door is under attack!")


door_1 = EntranceDoor('shut', 1.9)
table_1 = TableToSell('wood', 0.9, 'dinner', 15)
table_2 = TableSale('metal', 1, 'bedside', 17)
print(table_2)
table_2.sale()
print(table_2)
door_1.rob()
print(table_1)
table_2.sell()
print(table_2)