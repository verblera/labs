'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
biggest = 1
for x in range(0,3):
    word = input('Please, type a word: ')
    print(len(word), ', ', word)
    length = len(word)
    if length > biggest:
        biggest = length
        longest = word
    x=x+1
print('the longest word is ', longest)