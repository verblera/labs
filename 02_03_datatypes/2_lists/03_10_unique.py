'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# this piece of code works only if there are even numbers of repetitive elements,
# works well for the given example but not globally

check_list = []
for item in list_:
    if item in check_list:
        check_list.remove(item)
    else:
        check_list.append(item)
print(check_list)

# this is a longer code which works for all cases:
dict_ = {}

unique = list()
for key in list_:
    if key in dict_:
        dict_[key] += 1
    else:
        dict_[key] = 1

for k, v in dict_.items():
    if v == 1:
        unique.append(k)
print(unique)
