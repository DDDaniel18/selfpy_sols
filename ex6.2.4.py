def extend_list_x(list_x, list_y):
    """
    :param list_x:
    :type list_x: list

    :param list_y:
    :type list_y: list
    :return list_x after inserting list_y in the beginging
    :rtype list
    """
    list_x[:0] = list_y
    return list_x


def main():
    x = [4, 5, 6]
    y = [1, 2, 3]
    print(extend_list_x(x, y))
    print(x)


if __name__ == '__main__':
    main()
