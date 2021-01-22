'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
sum = 0
start_num = int(input('Please type in the first number: '))
end_num = int(input('Please type in the lst number: '))
for x in range (start_num, (end_num+1)):
    sum += x
print(sum)