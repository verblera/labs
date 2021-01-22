'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]


def summa(listik):
    s = 0
    for i in listik:
        s += i
    return s


def stats(list_):
    # define the function here
    max_num = max(list_)
    min_num = min(list_)
    sum_num = summa(list_)
    av_num = sum_num / len(list_)
    return max_num, min_num, sum_num, av_num

# call the function below here

print(stats(example_list))
