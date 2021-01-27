'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class Car:

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"A car model {self.model} is released in {self.year} and has a maximum speed {self.max_speed}."

    def speed_increase(self):
        self.max_speed = self.max_speed + 5


car_1 = Car('Volvo', 2008, 190)
car_2 = Car('Renault', 2011, 190)
car_3 = Car('Tesla', 2019, 270)
print(f'{car_1}\n{car_2}\n{car_3}')
car_1.speed_increase()
print(car_1)
