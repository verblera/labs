'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 5
i = 1
string = ''
while n > 0:
    string += '*'* i + '\n'
    n -= 1
    i += 1
print(string)