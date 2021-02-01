"""
Write a script with a function that demonstrates the use of **kwargs.

"""

def names(**kwargs):
    with open('names.txt', 'w') as facebook:
        for name, familyname in kwargs.items():
            facebook.write(f'{name} {familyname}\n')


names(Anna = 'Smith', James = 'Bond', Sherlock ='Holmes', Donald = 'Trump', Sebastian = 'Kurz', Lady = 'Gaga')
