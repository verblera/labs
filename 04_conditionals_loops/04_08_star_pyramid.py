'''
Write a script that takes in a number from the user as input and prints the following structure.

Suppose the input is 5, you will output
*
* *
* * * 
* * * *
* * * * * 
i.e. number of rows will be 5, 1st row will have 1 star, 2nd row will have 2 stars, 3rd row 3 stars, 4th row will have 4 stars and 5th row will have 5 stars.

Another example: if input is 3, you will output
*
* *
* * *

Hint: Think of nested for loops

'''

# not sure how it is different from the first exercises apart form taking a number from an user
n = int(input('PLease type in a number: '))
i = 1
string = ''
while n > 0:
    string += '*' * i + '\n'
    n -= 1
    i += 1
print(string)