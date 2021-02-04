"""
Write a decorator function that wraps text passed to it in a html <p> tag.

"""


def my_decorator(func):
    def wrapper():
        print(f"<p> {func()} </p>")
    return wrapper


@my_decorator
def hello():
    return "Hello!"


hello()


# wrapping a user's input
def my_decorator2(func):
    def wrapper(*args):
        print(f"<p> {func(args)[0][0]} </p>")
    return wrapper


@my_decorator2
def insert(*args):
    return args


insert(input('What do you want to wrap? '))