def show_hidden_word(secret_word, old_letters_guessed):
    result = ''
    for c in secret_word:
        if c in old_letters_guessed:
            result += c
        else:
            result += '_'
        result += ' '
    return result


def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))
    # m _ m m _ _ s

if __name__ == '__main__':
    main()