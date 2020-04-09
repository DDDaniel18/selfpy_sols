def numbers_letters_count(my_str):
    digits = 0
    for c in my_str:
        if c in '0123456789':
            digits += 1
    return digits, len(my_str) - digits


def main():
    print(numbers_letters_count("Python 3.6.3"))
    # [3, 9]


if __name__ == '__main__':
    main()