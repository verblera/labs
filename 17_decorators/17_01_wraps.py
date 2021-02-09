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
    def wrapper(returned_value):
        return f"<p> {func(returned_value)} </p>"
    return wrapper


@my_decorator2
def insert(user_input):
    return user_input


print(insert(input('What do you want to wrap in a p tag? ')))
