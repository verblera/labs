"""
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

"""

def my_enumerate(lists):
    i = 1
    new_list = []
    for item in lists:
        tupl = (i, item)
        new_list.append(tupl)
        i += 1
    return new_list


list_ = ['banana bread', 'carrot cake', 'pancakes', 'danish']
print(my_enumerate(list_))