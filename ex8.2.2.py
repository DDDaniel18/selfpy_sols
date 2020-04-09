def get_price(t):
    return t[1]


def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=get_price, reverse=True)


def main():
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(sort_prices(products))
    # [('bread', '9.0'), ('milk', '5.5'), ('candy', '2.5')]


if __name__ == '__main__':
    main()