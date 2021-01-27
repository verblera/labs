"""
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
"""

with open('words.txt', 'r') as text:
    words = text.read().split()

for word in words:
    if len(word) > 20:
        print(word)