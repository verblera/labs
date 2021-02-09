"""
Write a decorator function that wraps text passed to it in a html <p> tag.

"""


def my_decorator(func):
    def wrapper():
        return f"<p> {func()} </p>"
    return wrapper


@my_decorator
def hello():
    return "Hello!"


print(hello())


# wrapping a user's input
def my_decorator2(func):
    def wrapper(*args):
        return f"<p> {func(args)[0]} </p>"
    return wrapper


@my_decorator2
def insert(a):
    return a


print(insert(input('What do you want to wrap? ')))