"""
Write a script that demonstrates a try/except/else.

"""
string = '5'
try:
    number = int(string)
except ValueError:
    print('cannot do it')
else:
    print(number)
