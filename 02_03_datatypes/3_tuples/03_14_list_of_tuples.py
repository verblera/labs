'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
list_ = list()
string = input('PLease type in a sentence: ')
words = string.split()
for word in words:
    list_.append(tuple(word))
print(list_)