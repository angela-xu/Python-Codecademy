'''
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay". 
So "Python" becomes "ythonpay".
'''

print('Welcome to Pig Latin Game')
pyg = 'ay'
word = input('Please enter a word:')    # Ask the user to enter a word

if len(word) > 0 and word.isalpha():    # Check if the word has and only has characters
    word = word.lower()
    first = word[0]
    new_word = word[1:] + first + pyg
    print(new_word)
else:
    print('invalid word')
