def chocolate_maker(small, big, x):
    return x // 5 <= big and x % 5 <= small


print(chocolate_maker(3, 1, 8))   # True
print(chocolate_maker(3, 1, 9))   # False
print(chocolate_maker(3, 2, 13))  # False
