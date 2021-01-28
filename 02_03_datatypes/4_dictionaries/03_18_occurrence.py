'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

dict_ = {}

user_input = input('Please type in: ')
for letter in user_input:
    if letter in dict_:
        dict_[letter] += 1
    else:
        dict_[letter] = 1
print(dict_)