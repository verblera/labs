'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
numbers = list()
for x in range(1, 11):
    number = int(input('Please, type a number: '))
    numbers.append(number)
print(numbers)
odd = [1, 3, 5, 7, 9]
even = [8, 6, 4, 2, 0]
sorted_numbers = list()
for o in odd:
    sorted_numbers.append(numbers[o])
for e in even:
    sorted_numbers.append(numbers[e])
print(sorted_numbers)