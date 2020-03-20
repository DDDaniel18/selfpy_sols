def distance(num1, num2, num3):
    is2_close = abs(num2 - num1) <= 1
    is3_close = abs(num3 - num1) <= 1
    return (is2_close and not is3_close) or (is3_close and not is2_close) and abs(num3 - num2) >= 2


print(distance(1, 2, 10))

print(distance(4, 5, 3))

