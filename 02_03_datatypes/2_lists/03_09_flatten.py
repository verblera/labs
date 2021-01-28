'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
list_ = list()
starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for x in range(0, len(starting_list)):
    for y in range(0, len(starting_list[x])):
        list_.append(starting_list[x][y])
print(list_)