def arrow(my_char, max_length):
    result = []
    for row_len in range(1, max_length):
        result.append(my_char*row_len)
    for row_len in range(max_length, 0, -1):
        result.append(my_char*row_len)
    return "\n".join(result)


def main():
    print(arrow('*', 5))


if __name__ == '__main__':
    main()
