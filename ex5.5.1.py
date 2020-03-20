def is_valid_input(letter):
    """
    checks if the letter is valid guess,
    single letter in english
    :param letter:
    :type letter: str
    :return: True if valid
    :rtype bool
    """
    return len(letter) == 1 and letter.lower() in 'abcdefghijklmnopqrstuvwxyz'


def main():
    print(is_valid_input('a'))  # True
    print(is_valid_input('A'))  # True
    print(is_valid_input('$'))  # False
    print(is_valid_input("ab"))  # False
    print(is_valid_input("app$"))  # False


if __name__ == '__main__':
    main()
