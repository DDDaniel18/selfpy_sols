def check_win(secret_word, old_letters_guessed):
    for c in secret_word:
        if c not in old_letters_guessed:
            return False
    return True


def main():
    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessed))
    # False

    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))
    #True


if __name__ == '__main__':
    main()