'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

numbers = input('Please type in numbers splitting them ONLY with space: ')
num_list = numbers.split()
for x in range(0, len(num_list)):
    num_list[x] = int(num_list[x])
num_list.sort()
print(num_list)
if len(num_list) % 2 != 0:
    num_list.append(0)
print_list = list()
for i in range(0, (len(num_list)-1), 2):
    tuple_ = (num_list[i], num_list[i+1])
    print_list.append(tuple_)
print(print_list)