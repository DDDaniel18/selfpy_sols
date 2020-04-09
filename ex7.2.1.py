def is_greater(my_list, n):
    result = []
    for item in my_list:
        if item > n:
            result.append(item)
    return result


def main():
    result = is_greater([1, 30, 25, 60, 27, 28], 28)
    print(result)
    # [30, 60]


if __name__ == '__main__':
    main()