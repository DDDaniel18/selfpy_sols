def func(num1, num2):
    """
    return average of num1 and num2
    :param num1: number
    :type num1: float or int
    :param num2: number
    :type num2: float or int
    :return average of num1 and num2
    :rtype float
    """
    return (num1 + num2) / 2


def main():
    print(func(11, 30))  # will print 20.5
    help(func)


if __name__ == "__main__":
    main()
