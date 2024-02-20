def calculate_sum():
    total_sum = 0

    for i in range(2, 101):
        for j in range(2, 101):
            total_sum += pow(i, j)

    return total_sum

result = calculate_sum()
print(result)
