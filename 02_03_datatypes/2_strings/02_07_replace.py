'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

sentence = (input('type your sentence: ')).lower()
symbol = input('type a symbol: ')
i = 0
new_sentence=''
for letter in sentence:
    if letter == sentence[0]:
        new_sentence = new_sentence+symbol
    else:
        new_sentence = new_sentence + sentence[i]
    i=i+1
print(new_sentence)

#option 2

new_sentence2 = sentence.replace(sentence[0],symbol)
print(new_sentence2)