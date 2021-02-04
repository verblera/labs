"""
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

"""


def my_decorator2(func):
    def wrapper(*args):
        return f"<{func(args)[0][1]}> {func(args)[0][0]} <\{func(args)[0][1]}>"
    return wrapper


@my_decorator2
def insert(*args):
    return args

print(insert(input('Please, print in a sentence: '),
       input('Please, print in a tag: ')))