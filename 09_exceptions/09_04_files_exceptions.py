"""
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

"""


class MyException(Exception):

    def __init__(self, value):
        self.value = value


books = ('books/war_and_peace.txt', 'books/pride_and_prejudice.txt', 'books/crime_and_punishment.txt',
         'books/crime_and_punishment2.txt')

# first exercise: opening war & peace and storing text as var:
try:
    with open(books[0], 'r', encoding='utf8') as text:
        war_peace = text.read()
        print('a variable stores a whole text ', len(war_peace), ' characters long')
# second exercise
    # replacing content of crime and punishment with an empty string (in cr_and_pun2.txt)
    with open(books[-1], 'w') as text:
        text.write('')

# third exercise: looping over files and printing the first characters:

    for book in books:
        with open(book, 'r', encoding='utf8') as text:
            a = text.readline()
            print('first character: ', a[0])

except UnicodeDecodeError:
    print('Some troubles with decoding ', book, '....')
except FileNotFoundError:
    print('Check the directory! ', book)
except IndexError:
    print('Seems like your file ', book, ' is too short!')

#Bonus challenge
# does not work if put in another place
try:
    for item in books:
        with open(item, 'r', encoding='utf8') as lines:
            b = lines.readline()
            if 'Prince' in b:
                # I can raise it but fail to give a book's title
                raise MyException(item)


except MyException as PrinceBook:
    print('A word Prince is in ', PrinceBook)
