def sequence_del(my_str):
    result = ''
    last_str = ''
    for c in my_str:
        if c != last_str:
            result = result + c
            last_str = c
    return result


def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    # 'python'
    print(sequence_del("SSSSsssshhhh"))
    # 'Ssh'
    print(sequence_del("Heeyyy   yyouuuu!!!"))
    # 'Hey you!'


if __name__ == '__main__':
    main()
