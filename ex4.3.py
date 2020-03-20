# continue of ex3.5.py

HANGMAN_ASCII_ART = '''
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |                      
                     |___/
'''
MAX_TRIES = 6
print(HANGMAN_ASCII_ART + '\n' + str(MAX_TRIES))

# commenting this, since this is not required for this specifc exercise

# word_to_guess = input('Please enter a word: ')
# print('_ ' * len(word_to_guess))

guess = input('Guess a letter: ')

guess_lower = guess.lower()

# this is the more correct way we found to check if something is in english
if len(guess_lower) == 1 and guess_lower in 'abcdefghijklmnopqrstuvwxyz':
    print(guess_lower)
else:
    # if we are here, then something is wrong, we need to find the reason
    # However, the logic in the exercise is bit complicated, and we are not sure
    # there is correct way to implement it using the material so far
    # if there is better way, please write
    if len(guess_lower) == 1:
        print('E2')
    # this is 100% right, since it does not check only for english
    elif guess_lower.isalpha():
        print('E1')
    else:
        print('E3')

