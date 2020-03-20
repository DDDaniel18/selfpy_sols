def shift_left(my_list):
    """
    shifts list of 3 elements to the left
    :param my_list: list of len 3
    :type list
    :return: list of len3, shifted left
    :rtype list
    """
    a, b, c = my_list
    return [b, c, a]


def main():
    print(shift_left([0, 1, 2]))
    print(shift_left(['monkey', 2.0, 1]))


if __name__ == '__main__':
    main()
