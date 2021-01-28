'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
numbers = list()
for x in range(1, 11):
    number = int(input('Please, type a number: '))
    numbers.append(number)
print(numbers)
print(max(numbers))

i = 0
product = 1
while i < len(numbers):
    product *= numbers[i]
    i += 1
print(product)