"""
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

"""
try:
    number1 = int(input('Please, type in a number 1: '))
    number2 = int(input('Please, type in a number 2: '))
    print(number1/number2)
except ZeroDivisionError:
    print('cannot divide by 0')
except ValueError:
    print('we need a number, not a word!')