'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
my_number = 0
number = int(input('PLease, type in a number: '))
while my_number != number:
    print('searching...')
    my_number += 1
print(my_number)