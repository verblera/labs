"""
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
"""

with open('words.txt', 'r') as text:
    words = text.readlines()

words = reversed(words)
new_text = open('words_reverse.txt', 'x')
for word in words:
    new_text.write(word)

new_text.close()
