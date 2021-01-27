'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''


class Planet:
    def __init__(self, name, size, temperature, place):
        self.name = name
        self.size = size
        self.temperature = temperature
        self.place = place

    def __str__(self):
        return f'{self.name.capitalize()} is a {self.place} planet in the Solar system.\n'\
               f'The average temperature there is {self.temperature}.\nThe size is {self.size}'


Earth = Planet('Earth', 6371, 14.9, 3)
print(Earth)
