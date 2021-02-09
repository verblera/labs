"""
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

"""

def tagging(tag):
    def my_decorator2(func):
        def wrapper(*args):
            return f'<{tag}> {func(*args)} <\{tag}>'
        return wrapper
    return my_decorator2


@tagging('strong')
def strong(sentence):
    return sentence

@tagging('div')
def div(a,b):
    return a + b

print(strong(input('Type in a sentence: ')))
print(div('This is a division',' tag'))