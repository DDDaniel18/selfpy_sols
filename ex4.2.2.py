word = input('Enter a word: ')
word_to_check = word.lower().replace(' ', '')
if word_to_check == word_to_check[::-1]:
    print('OK')
else:
    print('NOT')
