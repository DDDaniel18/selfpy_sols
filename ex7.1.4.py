def squared_numbers(start, stop):
    result = []
    while start <= stop:
        result.append(start**2)
        start += 1
    return result


def main():
    print(squared_numbers(4, 8))
    # [16, 25, 36, 49, 64]
    print(squared_numbers(-3, 3))
    # [9, 4, 1, 0, 1, 4, 9]


if __name__ == '__main__':
    main()