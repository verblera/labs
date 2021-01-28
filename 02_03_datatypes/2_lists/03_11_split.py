'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

sentence = input('Type in a text: ').lower()
list_ = sentence.split()
print(list_)
most_common = max(list_, key = list_.count)
print(most_common)