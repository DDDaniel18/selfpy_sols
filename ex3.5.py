# continue of ex2.5.py

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

word_to_guess = input('Please enter a word: ')
print('_ ' * len(word_to_guess))


