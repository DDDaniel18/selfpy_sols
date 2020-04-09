def main_loop(products):
    while True:
        choice = int(input('Please enter choices (1-9): '))
        if choice == 1:
            for product in products:
                print(product)
        elif choice == 2:
            print(len(products))
        elif choice == 3:
            product = input('Please enter product to check if in list: ')
            print(product in products)
        elif choice == 4:
            product = input('Please enter product to count: ')
            print(products.count(product))
        elif choice == 5:
            product = input('Please enter product to remove: ')
            if product in products:
                products.remove(product)
        elif choice == 6:
            product = input('Please enter product to add: ')
            products.append(product)
        elif choice == 7:
            for product in products:
                if not is_legal(product):
                    print(product)
        elif choice == 8:
            products = remove_dups(products)
            print('Duplicated removed')
        elif choice == 9:
            print('Bye')
            break


def is_legal(product):
    if len(product) < 3:
        return False
    for c in product:
        if c.lower() not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True


def remove_dups(products):
    result = []
    for p in products:
        if p not in result:
            result.append(p)
    return result


def main():
    products = input('Please enter products list: ')
    main_loop(products.split(","))

if __name__ == '__main__':
    main()
