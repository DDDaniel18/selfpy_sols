def sort_anagrams(list_of_words):
    result = []
    for w in list_of_words:
        found = False
        for sublist in result:
            if sorted(sublist[0]) == sorted(w):
                sublist.append(w)
                found = True
                break
        if not found:
            result.append([w])
    return result



def main():
    list_of_words = [
        'deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating',
        'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening',
        'lasted', 'resmelts'
    ]
    print(sort_anagrams(list_of_words))
    assert sort_anagrams(list_of_words) == [['deltas', 'desalt', 'slated', 'salted', 'staled', 'lasted'], ['retainers', 'ternaries'], ['pants'], ['generating', 'greatening'], ['smelters', 'termless', 'resmelts']]


if __name__ == '__main__':
    main()
