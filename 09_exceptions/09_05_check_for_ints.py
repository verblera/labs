"""
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

"""
true = True
while true:
    number = input('Please type in a number: ')
    try:
        number = int(number)
        print('Ok, it was an integer')
        true = False
    except ValueError:
        print('I told a NUMBER, not ', number)
