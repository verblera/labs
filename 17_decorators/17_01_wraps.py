"""
Write a decorator function that wraps text passed to it in a html <p> tag.

"""


def p_tag(msg):
    def wrapping():
        return f'<p> {msg} </p>'
    return wrapping


string = input('Please, type in a sentence: ')
a = p_tag(string)
print(a())
