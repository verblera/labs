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
