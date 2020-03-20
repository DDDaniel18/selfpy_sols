digits = input("Enter three digits (each digit for one pig): ")

pig1 = int(digits[0])
pig2 = int(digits[1])
pig3 = int(digits[2])

sum_pigs = pig1 + pig2 + pig3

print(sum_pigs)
print(sum_pigs // 3)
print(sum_pigs % 3)
print(sum_pigs %3 == 0)


