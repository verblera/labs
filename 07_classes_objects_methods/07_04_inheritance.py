"""
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

"""


class Movie:

    def __init__(self, year, title, status='to watch'):
        self.year = year
        self.title = title
        self.status = status

    def watched(self):
        self.status = 'watched'


class RomCom(Movie):

    def __str__(self):
        return f'"{self.title}" is a romantic comedy ({self.year}). {self.status}'


class ActionMovie(Movie):

    def __init__(self, year, title, status, pg=13):
        super().__init__(year, title, status)
        self.pg = pg

    def __str__(self):
        return f'"{self.title}" is an action movie ({self.status},{self.year}, rated {self.pg})'


film_1 = RomCom(2013, 'Her', 'to watch')
film_2 = RomCom(1999, 'She\'s All That', 'to watch')
film_3 = ActionMovie(2018, 'Black Panther', 'watched')
film_4 = ActionMovie(2019, 'Avengers', 'to watch')
print(film_1)
film_1.watched()
print(film_1)