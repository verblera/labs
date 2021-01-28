'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

x = 5
y= 7.5
print(type(float(x)), float(x))
print(type(int(y)), int(y))
print(y//5)
a = int(input('type the first number'))
b = int(input('type the second number'))
print(a*b)