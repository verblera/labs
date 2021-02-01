"""
Write a simple aggregate function, sum(), that takes a list a returns the sum.

"""


def summing(lists):
    summed = 0
    for x in lists:
        summed += x
    return summed


list_ = [2, 6, 7, 9, 11, 23, 23]
y = summing(list_)
print(y)