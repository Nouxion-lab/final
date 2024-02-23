
result = 2**1337
result_str = str(result)
digit_sum = 0

for digit in result_str:
    digit_sum += int(digit)

print(f'2^1337 = {result}')
print(f'Sum of digits: {digit_sum}')

