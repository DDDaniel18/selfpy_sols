def format_list(my_list):
    """
    :param my_list: list of string of even length
    :type my_list: list
    :return: concatenation of the even elements with ", " and "and" for the last one
    :rtype str
    """
    return ", ".join(my_list[:-1:2]) + " and " + my_list[-1]


def main():
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    print(format_list(my_list))  # hydrogen, lithium, boron, and magnesium


if __name__ == '__main__':
    main()
