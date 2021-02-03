"""
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

"""


def tagging(msg, tag):
    def wrapping():
        return f'<{tag}> {msg} </{tag}>'
    return wrapping


string = input('Please, type in a sentence: ')
tg = input('Please, type in an HTML tag you want: ')
a = tagging(string, tg)
print(a())
