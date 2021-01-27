"""
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


"""

with open('words.txt', 'r') as text:
    words = text.read().split()

short_words = []
long_words = []
long_word = ''
short_word = words[0]
print(f'The total number of words is {len(words)}.')
for word in words:
    if len(word) > len(long_word):
        long_word = word
    elif len(word) < len(short_word):
        short_word = word
    else:
        pass

for word in words:
    if len(word) == len(short_word):
        short_words.append(word)
    elif len(word) == len(long_word):
        long_words.append(word)
    else:
        pass

print(f'Shortest words are {short_words}\nLongest words are {long_words}')