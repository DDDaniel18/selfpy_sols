def seven_boom(end_number):
    result = []
    for n in range(0, end_number+1):
        if n % 7 == 0 or '7' in str(n):
            result.append('BOOM')
        else:
            result.append(n)
    return result


def main():
    print(seven_boom(17))
    # ['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM', 15, 16, 'BOOM']


if __name__ == '__main__':
    main()