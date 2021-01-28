'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
vowels = ['e','o','a','i', 'y','u']
count = 0
sentence = input('What is your sentence today? ')
for letter in sentence:
    if letter in vowels:
        count = count + 1
print(count)

vowels_dic = {'e': 0,'o': 0,'a': 0,'i':0, 'y':0,'u':0}
for letter in sentence:
    if letter in vowels_dic.keys():
        vowels_dic[letter]=vowels_dic[letter]+1
for key, value in vowels_dic.items():
    print(key, value)

