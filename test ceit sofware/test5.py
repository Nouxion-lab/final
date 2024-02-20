memo = {}

def fibonacci(i):
    if i in memo:
        return memo[i]
    
    if i == 0:
        result = 0
    elif i == 1:
        result = 1
    else:
        result = fibonacci(i-2) + fibonacci(i-1)

    memo[i] = result
    return result

def sum_odd_fibonacci_numbers(limit):
    odd_sum = 0
    for x in range(limit):
        fib_number = fibonacci(x)
        if fib_number % 2 != 0:
            odd_sum += fib_number
    return odd_sum

result = sum_odd_fibonacci_numbers(100)
print(f"ผลรวมของเลขคี่ในรอบ 100 ของลำดับ Fibonacci คือ: {result}")